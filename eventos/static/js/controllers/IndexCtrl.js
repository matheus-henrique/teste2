app.controller('IndexCtrl',function($scope, $http,$uibModal,$window, $rootScope){
	$rootScope.vm = {};
	$rootScope.vm.alwaysShowCount = 0; 	
	console.log(window.user_id);
	
	$http.get("/notifications/"+window.user_id+"/").success(function(data){
		$rootScope.notifications = data;
		$rootScope.quantNotifications = $rootScope.notifications.length;
		for(i = 0; i < data.length;i++){
			if ((data[i].lido) && (i == data.length - 1)){
				$rootScope.vm.alwaysShowCount = 0;
			}else if(!data[i].lido){
				$rootScope.vm.alwaysShowCount++;
			}
		}
	});

	$scope.kaka = function(){
		$http.defaults.headers.put['X-CSRFToken'] = window.csrf_token;
		$http.put("/notifications/"+window.user_id+"/").success(function(data){

		});
	}

	
	var myModalLoginCtrl = function($http,$cookies,$scope, $uibModalInstance){
		$http.defaults.headers.post['X-CSRFToken'] = window.csrf_token;
		$scope.logar = function(){
			$http.post("/teste-login/",{"username":$scope.user,"password":$scope.pass}).success(function(data){
				$uibModalInstance.close();
				$window.location.href = '/perfil/';

			}).error(function() {
				console.log("Ocorreu um erro");
			});
		}
	}

	myModalLoginCtrl.$inject = ['$http','$cookies','$scope', '$uibModalInstance'];


	$scope.abrirLogin = function() {
		var modalInstance = $uibModal.open({
			ariaLabelledBy: 'modal-dialog',
				ariaDescribedBy: 'modal-body',
				templateUrl: '/static/eventos/views/modaLogin.html',
				animation: true,
				size : 'sm',
				controller : myModalLoginCtrl,
				
		});

	}
});




