import json
import logging
from odoo import http
from odoo.http import request, Response

_logger = logging.getLogger(__name__)


class TodoController(http.Controller):

    # --- Backend: Halaman web publik ---

    @http.route('/tugas', auth='public', website=True)
    def index(self, **kw):
        tasks = request.env['todo_list.task'].sudo().search([])
        return request.render('todo_list.halaman_tugas_ui', {'tasks': tasks})

    # --- API: CRUD sederhana ---

    @http.route('/api/tasks', auth='user', type='http', methods=['GET'], csrf=False)
    def get_all(self, limit=10, offset=0, **kw):
        tasks = request.env['todo_list.task'].search([], limit=int(limit), offset=int(offset))
        return self._json(200, [self._serialize(t) for t in tasks])

    @http.route('/api/tasks', auth='user', type='http', methods=['POST'], csrf=False)
    def create(self, **kw):
        data = json.loads(request.httprequest.data or '{}')
        if not data.get('name'):
            return self._json(400, error='Field "name" wajib diisi')
        task = request.env['todo_list.task'].create({'name': data['name'], 'description': data.get('description', '')})
        return self._json(201, self._serialize(task))

    @http.route('/api/tasks/<int:task_id>', auth='user', type='http', methods=['PUT'], csrf=False)
    def update(self, task_id, **kw):
        task = request.env['todo_list.task'].browse(task_id)
        if not task.exists():
            return self._json(404, error='Task tidak ditemukan')
        data = json.loads(request.httprequest.data or '{}')
        task.write({k: v for k, v in data.items() if k in ('name', 'description', 'is_done')})
        return self._json(200, self._serialize(task))

    @http.route('/api/tasks/<int:task_id>', auth='user', type='http', methods=['DELETE'], csrf=False)
    def delete(self, task_id, **kw):
        task = request.env['todo_list.task'].browse(task_id)
        if not task.exists():
            return self._json(404, error='Task tidak ditemukan')
        task.unlink()
        return self._json(200, {'deleted': True})

    # --- Helper ---

    def _serialize(self, task):
        return {'id': task.id, 'name': task.name, 'description': task.description or '', 'is_done': task.is_done, 'user': task.user_id.name}

    def _json(self, status, data=None, error=None):
        body = {'data': data} if data is not None else {'error': error}
        return Response(json.dumps(body), status=status, mimetype='application/json')
