//Opciones entre Lente y Otro Producto.
console.log("generar_pedido.js is loaded");

$(document).ready(function() {
    $("#opcionesLente").change(function () {
        if ($(this).val() == "lente") {
            //Si opcionesLente == "lente", muestra los campos inputFarClose, inputLeftRight e inputArmazon. Se esconde inputProducto.
            $("#inputsLente").show();
            $("#inputsOtroProducto").hide();
            $("#inputProducto").removeAttr("required");
            $("#inputProducto").removeAttr("data-error");
            $("#inputFarClose").attr("required", "");
            $("#inputFarClose").attr("data-error", "This field is required.");
            $("#inputLeftRight").attr("required", "");
            $("#inputLeftRight").attr("data-error", "This field is required.");
            $("#inputArmazon").attr("required", "");
            $("#inputArmazon").attr("data-error", "This field is required.");
        } else {
            //Si opcionesLente == "lente", muestra los campos inputFarClose, inputLeftRight e inputArmazon. Se esconde inputProducto.
            $("#inputsLente").hide();
            $("#inputsOtroProducto").show();
            $("#inputFarClose").removeAttr("required");
            $("#inputFarClose").removeAttr("data-error");
            $("#inputLeftRight").removeAttr("required");
            $("#inputLeftRight").removeAttr("data-error");
            $("#inputArmazon").removeAttr("required");
            $("#inputArmazon").removeAttr("data-error");
            $("#inputProducto").attr("required", "");
            $("#inputProducto").attr("data-error", "This field is required.");
        }
    });
    $("#opcionesLente").trigger("change");  //Cuando cambia el estado, se ejecuta el evento change().
});

function run() {

    var e = document.getElementById("opcionesLente");
    //var e_text = e.options[e.selectedIndex].text;

    console.log("Opción elegida:" + e.value);

    var str1 = "Resultado: ";
    var mid = " - ";
    var calculo_id = 0;

    //En caso del tipo ser "lente", calcula el id en función de las opciones seleccionadas.
    if (e.value == "Lente") {
        console.log("ES LENTE");

        var e1 = document.getElementById("inputFarClose");
        var e1_text = e1.options[e1.selectedIndex].text.toLowerCase();
        console.log("e1_text:" + e1_text);
        if (e1_text == "cerca") {
            calculo_id += 4;
        } else {
            calculo_id += 0;
        }

        var e2 = document.getElementById("inputLeftRight");
        var e2_text = e2.options[e2.selectedIndex].text.toLowerCase();
        console.log("e2_text:" + e2_text);
        if (e2_text == "derecha") {
            calculo_id += 2;
        } else {
            calculo_id += 0;
        }

        var e3 = document.getElementById("inputArmazon");
        var e3_text = e3.options[e3.selectedIndex].text.toLowerCase();
        console.log("e3_text:" + e3_text);
        if (e3_text == "sin armazón") {
            calculo_id += 1;
        } else {
            calculo_id += 0;
        }

        calculo_id += 1;

        document.getElementById("texto").innerHTML = str1.concat(
            e_text," ",e1_text,mid,e2_text,mid,e3_text,"(id = ",calculo_id,")"
        );
    } else {
        document.getElementById("texto").innerHTML = str1.concat(e_text);
    }

    var valor = document.getElementById("texto").innerHTML;
    var valor = valor.replace("Resultado: ", "");
    var valor = valor.replace("ó", "o");
    console.log("Valor: " + valor);
}

function calculo_subtotal() {
    var cantidad = document.getElementById("inputCantidad").value;
    var precio = document.getElementById("inputPrecio").value;

    console.log("Cantidad: " + cantidad);
    console.log("Precio: " + precio);

    var subtotal = 0;

    if (cantidad > 0 && precio > 0) {
        var subtotal = (cantidad * precio).toFixed(2);
        console.log("SUBTOTAL = " + subtotal);

        document.getElementById("inputSubtotal").value = subtotal.toString();
    } else {
        document.getElementById("inputSubtotal").value = "0";
    }
}