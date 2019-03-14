var app = angular.module('app', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});


app.controller('ventaController', ['$scope', '$http', function($s, $h) {
    $s.venta="hola";
    console.log($s.venta)
    $s.mostrarResumen=function(){
        $('#resumenModal').modal('show')
    }
}]);