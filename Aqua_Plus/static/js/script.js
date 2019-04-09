var app = angular.module('app', []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});
app.controller('mainController', ['$scope', '$http', function ($s, $h) {
}]);

app.controller('loginController', ['$scope', '$http', function ($s, $h) {
    if (sessionStorage.getItem("user") !== null) {
        var data = JSON.parse(sessionStorage.getItem("user"));
        if (data.tipo == 2) {
            window.location.href = "../venta";
        } else {
            window.location.href = "../adminView";
        }
    }
    $s.login = function (correo, pass) {
        console.log("sjdjhas")
        var data = {
            correo: correo,
            pass: pass,
        }

        console.log(data)
        var token = document.getElementById('token').value;
        $.ajax({
            type: "POST",
            url: "/login/",
            headers: { "X-CSRFToken": token },
            data: data,
            dataType: "json",
            success: function (data) {
                console.log(data)
                if (data.error == 2) {
                    alert("Usuario o contrasena incorrecto")
                } else {
                    sessionStorage.setItem("user", JSON.stringify(data));
                    if (data.tipo == 2) {
                        window.location.href = "../venta";
                    } else {
                        window.location.href = "../adminView";
                    }
                }

            },
            failure: function (errMsg) {
                alert(errMsg);
            }
        });
    }
}]);
app.controller('adminController', ['$scope', '$http', function ($s, $h) {
    if (sessionStorage.getItem("user") === null) {
        window.location.href = "../";
    }
    $s.trabajadores = true;
    $s.reportes = false;
    $s.toggleMenu = function (opc) {
        if (opc == 1) {
            $s.trabajadores = true;
            $s.reportes = false;
        } else {
            $s.trabajadores = false;
            $s.reportes = true;
            $s.obtenerReportes();
        }
    }


    $s.cerrar = function () {
        sessionStorage.clear();
        window.location.href = "../";
    }
    $s.usuarios = {}
    $s.reportesArr=[];
    $s.obtenerReportes = function () {
        $h({
            method: 'GET',
            url: '../reportes/'
        }).then(function successCallback(response) {
            console.log(response);
            $s.reportesArr = response.data;
        });
    }

    $s.setData = function () {
        $h({
            method: 'GET',
            url: '../usuarios/'
        }).then(function successCallback(response) {
            var obj = JSON.parse(response.data.message)
            console.log(obj);
            $s.usuarios = obj;
        });
    }
    $s.setData();

    $s.tempUsuario = -1;
    $s.abrirModalEliminarUsu = function (id) {
        console.log("eliminar id", id)
        $s.tempUsuario = id;
        $('#eliminarUsuario').modal('show')
    }
    $s.eliminarUsuario = function () {
        var data = {
            usuario: $s.tempUsuario,
        }
        console.log(data)
        var token = document.getElementById('token').value;
        $.ajax({
            type: "POST",
            url: "/eliminarUsuario/",
            headers: { "X-CSRFToken": token },
            data: data,
            dataType: "json",
            success: function (data) {
                console.log(data)
                if (data.error == 1) {
                    alert(data.msg);
                    $s.setData();
                    $('#eliminarUsuario').modal('hide')
                } else {
                    alert(data.msg);
                }
            },
            failure: function (errMsg) {
                alert(errMsg);
            }
        });
    }
    $s.guardarUsuario = function (correo, pass) {

        var data = {
            correo: correo,
            pass: pass,
        }
        console.log(data)
        var token = document.getElementById('token').value;
        $.ajax({
            type: "POST",
            url: "/usuarios/",
            headers: { "X-CSRFToken": token },
            data: data,
            dataType: "json",
            success: function (data) {
                console.log(data)
                if (data.error == 1) {
                    alert(data.msg);
                    $s.setData();
                    $('#agregar').modal('hide')
                } else {
                    alert(data.msg);
                }
            },
            failure: function (errMsg) {
                alert(errMsg);
            }
        });
    }
}]);
app.controller('ventaController', ['$scope', '$http', function ($s, $h) {
    $s.user = {};
    if (sessionStorage.getItem("user") === null) {
        window.location.href = "../";

    } else {
        $s.user = JSON.parse(sessionStorage.getItem("user"));
        console.log($s.user);
    }
    $s.tipo = 1;
    $s.cantidad = 1;

    $s.tipoVenta = {}
    $s.cerrar = function () {
        sessionStorage.clear();
        window.location.href = "../";
    }
    $s.setData = function () {

        $h({
            method: 'GET',
            url: '../getTipoVenta/'
        }).then(function successCallback(response) {
            var obj = JSON.parse(response.data.message)
            console.log(obj);
            $s.tipoVenta = obj;
        });
    }
    $s.setData();
    $s.getPrecio = function (id) {
        console.log("asjkdhakjs")
        console.log($s.tipo)
        console.log(id)
        var precio = -1;
        for (var precio of $s.tipoVenta) {
            console.log(precio)
            if (precio.pk == id) {
                precio = precio.fields.precio;
                break;
            }
        }
        return precio;
    }

    $s.mostrarResumen = function () {
        console.log($s.cantidad)
        if ($s.cantidad == "" || $s.cantidad == 0 || $s.cantidad == null) {
            alert("Inserte cantidad")
            return;
        }
        $('#resumenModal').modal('show')
    }

    $s.vender = function () {
        var user = $s.user;
        console.log(user);

        var data = {
            vendedor: user.id,
            tipo: $s.tipo,
            cantidad: $s.cantidad,
            total: $s.cantidad * $s.getPrecio($s.tipo),
        }
        console.log(data)

        var token = document.getElementById('token').value;
        $.ajax({
            type: "POST",
            url: "/vender/",
            headers: { "X-CSRFToken": token },
            data: data,
            dataType: "json",
            success: function (data) {
                console.log(data)
                if (data.error == 1) {
                    alert(data.msg);
                    $('#resumenModal').modal('hide')
                }
            },
            failure: function (errMsg) {
                alert(errMsg);
            }
        });
    }



}]);