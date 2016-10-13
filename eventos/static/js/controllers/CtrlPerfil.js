app.controller('CtrlPerfil',function($scope,$http,$window,$rootScope,$window,$uibModal){
	$scope.form = {};
	$scope.form.bCloseAlert = false;
	$rootScope.myForm = {};
	$rootScope.myForm.myevents = false;
	$rootScope.myForm.principals = true;
	$rootScope.menu = ['active',''];
	$rootScope.eventos = $http.get("/eventos/").success(function(data){
		$rootScope.even = data;
	});

	$rootScope.eventosuser = $http.get('/eventos/user/').success(function(data){
		$rootScope.eventouserquant = data;
	});

	$rootScope.meusEventos = function(){
		$rootScope.myForm.myevents = true;
		$rootScope.myForm.principals = false;
		$rootScope.menu[0] = '';
		$rootScope.menu[1] = 'active';
	}
	$rootScope.meusFavoritos = function(){
		$rootScope.myForm.myevents = false
		$rootScope.myForm.principals = true;
		$rootScope.menu[0] = 'active';
		$rootScope.menu[1] = '';
	}


	var myModalLoginCtrl = function($scope,$uibModalInstance,$http,items,$rootScope){
		$scope.confirmar = function(){
			$scope.items = items;
			$http({
				method:"DELETE",
				url:"/eventos/"+$scope.items.id+"/",
				headers:{'X-CSRFToken': window.csrf_token}
			}).success(function(){
				$uibModalInstance.close();
				$http.get('../eventos/user/').success(function(data){
					$rootScope.eventouserquant = data;
				}).error(function(){
					$window.location.reload();
				});
				$scope.items.bCloseAlert = true;
				
			}); 
		}

		$rootScope.fechar = function(){
			$uibModalInstance.close();
		}
	}

	myModalLoginCtrl.$inject = ['$scope','$uibModalInstance','$http','items','$rootScope'];

	$scope.abrirConfirmacao = function(id){
		$scope.form.id = id;
		var modalInstance = $uibModal.open({
				ariaLabelledBy: 'modal-dialog',
				ariaDescribedBy: 'modal-body',
				templateUrl: '../static/eventos/views/modalConfirmar.html',
				animation: true,
				controller : myModalLoginCtrl,
				resolve: {
					items: function(){
						return $scope.form
					}
				}
				
		});
	}


});