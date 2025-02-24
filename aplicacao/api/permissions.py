from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permite acesso de leitura para qualquer usuário, mas exige que o usuário seja administrador para modificar os dados.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Permite apenas leitura para qualquer usuário
            return True
        return request.user and request.user.is_staff  # Permite escrita apenas para admins
