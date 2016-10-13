app.controller('CtrlCadastroEvento', function($scope,$http,Upload,$rootScope){
	$rootScope.formData = {};
	$scope.hstep = 1;
  	$scope.mstep = 15;
  	$scope.ismeridian = true;
  	$rootScope.dinamic = 0;
  	$rootScope.etapa = { etapas : [true,false,false,false]};
  	$scope.etapa_atual = null;
  	$rootScope.estilomenu = ["is-active","progress_last","progress_last","progress_last"];
  	$rootScope.progress = "40";
  	$rootScope.estados = [];
  	$rootScope.count = 0;
  	$rootScope.selecionado = false;
  	$rootScope.sucesso = false;


  	$http.get("../../static/eventos/js/json/estados-cidades.json").success(function(data){
  		$rootScope.dados = data;
  	});

  	$scope.buscar = function(){
		$scope.digitado = true;
		
		if($rootScope.formData.cidade.length >= 4){
			$scope.ativo = true;

		}else{
			$scope.ativo = false;
		}
	}
  	
	$scope.mostrar = function(city){
		$rootScope.formData.cidade = city;
		$scope.ativo = false;
		$rootScope.selecionado = true;

	}

	$scope.proximo = function(value1,value2){
		$rootScope.etapa.etapas[value1] = false;
		$rootScope.etapa.etapas[value2] = true;
		$rootScope.estilomenu[value1] = "is-complete";
		$rootScope.estilomenu[value2] = "is-active";
	}


	$http.defaults.headers.post['X-CSRFToken'] = window.csrf_token;
	$scope.cadastrarEvento = function(){
		$scope.horamsm = $rootScope.formData.hora.getHours()
		if($rootScope.formData.hora.getMinutes() <= 9){
			$scope.horamsm = $scope.horamsm+":"+"0"+$rootScope.formData.hora.getMinutes();
		}else{
			$scope.horamsm = $scope.horamsm+":"+$rootScope.formData.hora.getMinutes();
		} 

		console.log($scope.horamsm);

		$scope.file = Upload.upload({
			url: '/eventos/',
			data:{
		        nome: $rootScope.formData.nome,
		        descricao: $rootScope.formData.descricao,
		        local: $rootScope.formData.local,
		        latitude: $rootScope.formData.latitude,
		        longitude: $rootScope.formData.longitude,
		        cidade: $rootScope.formData.cidade,
		        imagem: $rootScope.formData.imagem,
		        valor: $rootScope.formData.valor,
		        data: $rootScope.formData.data,
		        hora: $scope.horamsm,
		        estilos: $rootScope.formData.estilos
			}
		}).progress(function(evt){
			$rootScope.andamento = "Upando imagem..."
			$rootScope.dinamic = parseInt(evt.loaded / evt.total * 100, 10);
			if($rootScope.dinamic === 100){$rootScope.andamento = "Criando Evento..."}
		}).success(function(data){
			$rootScope.sucesso = true;
			$rootScope.result = data;
		});

	}
});