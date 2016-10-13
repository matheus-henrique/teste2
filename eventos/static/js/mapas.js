		var map;
		var endereco_user;
		var directionsDisplay; // Instanciaremos ele mais tarde, que será o nosso google.maps.DirectionsRenderer
		var directionsService = new google.maps.DirectionsService();


		
		 
		function initialize() {
			console.log("foi mizeravi");
		   directionsDisplay = new google.maps.DirectionsRenderer(); // Instanciando...
		   var latlng = new google.maps.LatLng(-18.8800397, -47.05878999999999);
		 
		   var options = {
		      zoom: 5,
		      center: latlng,
		      mapTypeId: google.maps.MapTypeId.ROADMAP
		   };
		 
		   map = new google.maps.Map(document.getElementById("mapa"), options);
		   directionsDisplay.setMap(map); // Relacionamos o directionsDisplay com o mapa desejado
		}
		 
		



		function xpto(){
			var end1 = "Teresina"
			var end2 = "Timon";
			var request = { // Novo objeto google.maps.DirectionsRequest, contendo:
		      origin: end1, // origem
		      destination: end2, // destino
		      travelMode: google.maps.TravelMode.DRIVING // meio de transporte, nesse caso, de carro
  			 };



  			directionsService.route(request, function(result, status) {
		    if (status == google.maps.DirectionsStatus.OK) { // Se deu tudo certo
		         directionsDisplay.setDirections(result); // Renderizamos no mapa o resultado
		      }
		   });
		}
		