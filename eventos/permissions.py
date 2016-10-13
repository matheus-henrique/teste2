from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsOwnerOrReadOnly(BasePermission):

	def has_permission(self, request, view):
		if request.method == "GET":
				return True
		if request.method == "POST":
			if(request.user.is_authenticated()):
				return True
			return False
		return request.user
	

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		elif request.method == "PUT" or request.method == "DELETE":
			if obj.author == request.user:
				return True
			return False