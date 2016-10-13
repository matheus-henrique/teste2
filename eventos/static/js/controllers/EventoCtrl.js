app.controller('EventoCtrl',function($scope,$http,$window,$rootScope){
	$scope.coment = null;
	$scope.ver = false;
	$scope.textoPresenca = 'Confirmar Presença';
	$window.initialize();
	$scope.comentarios = $http.get("/eventos/comentarios/"+$window.id).success(function(data){
		$scope.coment = data;
	});
	


	$scope.confirmarPresenca = function(){
		$scope.isPresenca = "disabled";
		$scope.textoPresenca = 'Presença Confirmada';
		$http.defaults.headers.put['X-CSRFToken'] = window.csrf_token;
		$http.put("/evento/confirmarpresenca/"+$window.id+"/").success(function(data){
			$window.location.reload();
		});
	}

	$scope.mostrarComentario = false;
	$scope.mostrar = function(index,comentario){
		$scope.mostrarComentario = [];
		$scope.mostrarComentario[index] = true;
		console.log(comentario)
		
	}


	$scope.enviarRespostaComentario = function(id_comentario,comentariotext){
		$http.defaults.headers.put['X-CSRFToken'] = window.csrf_token;
		console.log(comentariotext)
		$http.put("/eventos/comentarios/id/"+id_comentario+"/",{"resposta":comentariotext}).success(function(data){
			$scope.comentarios = $http.get("/eventos/comentarios/"+$window.id).success(function(data){
				$scope.coment = data;
			});
		});
	}




	$scope.enviarComentario = function(comentario){
		$http.defaults.headers.post['X-CSRFToken'] = window.csrf_token;
		$http.post("/eventos/comentarios/"+$window.id+"/",{"comentario":comentario}).success(function(data){
			$scope.comentarios = $http.get("/eventos/comentarios/"+$window.id).success(function(data){
				$scope.coment = data;
			});
		});
	}
});