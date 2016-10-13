app.controller("CtrlTelaEventos",function($scope,$http, $rootScope,$window){
	$http.get("/eventos/cidade/"+window.cidade+"/").success(function(data){
		$rootScope.eventos = data;
		console.log($rootScope.eventos.length);
	});
});