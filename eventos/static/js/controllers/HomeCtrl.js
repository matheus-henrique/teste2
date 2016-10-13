app.controller('CtrlHome',function($scope,$rootScope, $http,$window){
	$scope.evento = {}
	$http.get("static/eventos/js/json/estados-cidades.json").success(function(data){
			$scope.dados = data;

	});


	$scope.mostrarEventos = function(city){
		$window.location.href = '/eventos/cidades/'+city;
	}
	$scope.buscar = function(){
		$scope.digitado = true;
		
		if($scope.evento.texto_busca.length >= 4){
			$scope.ativo = true;
		}else{
			$scope.ativo = false;
		}
	};
});