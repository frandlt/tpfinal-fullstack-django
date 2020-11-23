var productos_serializados = JSON.parse('{{turnos_serializados | safe}}');

/* $("#seeAnotherFieldGroup").change(function() {
    if ($(this).val() == "yes") {
      $('#otherFieldGroupDiv').show();
      $('#otherField1').attr('required', '');
      $('#otherField1').attr('data-error', 'This field is required.');
      $('#otherField2').attr('required', '');
      $('#otherField2').attr('data-error', 'This field is required.');
    } else {
      $('#otherFieldGroupDiv').hide();
      $('#otherField1').removeAttr('required');
      $('#otherField1').removeAttr('data-error');
      $('#otherField2').removeAttr('required');
      $('#otherField2').removeAttr('data-error');
    }
  });
  $("#seeAnotherFieldGroup").trigger("change"); */
var calculo_id = 0;
  $("#opcionesLente").click(function () {
    if ($("#radio_button").is(":checked")) {
      alert("it's checked");
    }
  });
  
  $("#opcionesLente").change(function () {
    if ($(this).val() == "lente") {
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
      //$('#otherField1').attr('required', '');
      //$('#otherField1').attr('data-error', 'This field is required.');
      //$('#otherField2').attr('required', '');
      //$('#otherField2').attr('data-error', 'This field is required.');
    } else {
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
      //$('#otherField2').removeAttr('data-error');
      //$('#otherField1').removeAttr('required');
      //$('#otherField1').removeAttr('data-error');
      //$('#otherField2').removeAttr('required');
      //$('#otherField2').removeAttr('data-error');
    }
  });
  $("#opcionesLente").trigger("change");
  
  /*$("#seeAnotherFieldGroup").change(function() {
      if ($(this).val() == "yes") {
        $('#otherFieldGroupDiv').show();
        $('#otherField1').attr('required', '');
        $('#otherField1').attr('data-error', 'This field is required.');
        $('#otherField2').attr('required', '');
        $('#otherField2').attr('data-error', 'This field is required.');
      } else {
        $('#otherFieldGroupDiv').hide();
        $('#otherField1').removeAttr('required');
        $('#otherField1').removeAttr('data-error');
        $('#otherField2').removeAttr('required');
        $('#otherField2').removeAttr('data-error');
      }
    });
    $("#seeAnotherFieldGroup").trigger("change");*/
  
  function run() {
    console.log("La función run() está ejecutándose");
  
    //var e = document.getElementById("ddlViewBy").innerHTML[0];
    //console.log(e.value);
    var e = document.getElementById("seeAnotherFieldGroup");
    var e_text = e.options[e.selectedIndex].text;
    //var text = e.options[e.selectedIndex].text.toLowerCase();
    //console.log("EJEMPLO:" + e);
    console.log("Opción elegida:" + e.value);
  
    var str1 = "Resultado: ";
    var mid = " - ";
    
  
    if (e.value == "lente") {
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
        e_text,
        " ",
        e1_text,
        mid,
        e2_text,
        mid,
        e3_text,
        "(id = ",
        calculo_id,
        ")"
      );

      document.getElementById("hidden-input-id").value = calculo_id;

    } else {
      document.getElementById("texto").innerHTML = str1.concat(e_text);
    }
  
    var valor = document.getElementById("texto").innerHTML;
    var valor = valor.replace("Resultado: ", "");
    var valor = valor.replace("ó", "o");
    console.log("Valor: " + valor);
  }

var precio=0

  function buscar(){
    if (calculo_id<=8){
      var producto = productos.get(id=calculo_id);
      }else {
        var x = document.querySelector('#inputProducto').value;
        var producto = productos.get(id=x);
      }
      precio = parseFloat(producto.precio_actual);
      document.querySelector('#inputPrecio').value = precio;
  }

  
  function calculo_subtotal() {
    var cantidad = document.getElementById("inputCantidad").value;
    var precio = document.getElementById("inputPrecio").value;
  
    console.log("Cantidad: " + cantidad);
    console.log("Precio: " + precio);
  
    var subtotal = 0;
    var inicio_subtotal = "$ 0";
  
    if (cantidad > 0 && precio > 0) {
      var subtotal = (cantidad * precio).toFixed(2);
      console.log("SUBTOTAL = " + subtotal);
  
      document.getElementById("inputSubtotal").value = subtotal.toString();
  
      //console.log(new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(subtotal));
  
      //document.getElementById("inputSubtotal").value = Intl.NumberFormat('es-AR', { style: 'number', currency: 'ARS' }).format(subtotal).toString();
  
      //document.getElementById("inputSubtotal").value = inicio_subtotal.concat(subtotal.toString());
    } else {
      //document.getElementById("inputSubtotal").value = inicio_subtotal.concat("0");
      document.getElementById("inputSubtotal").value = "0";
    }
  }

  