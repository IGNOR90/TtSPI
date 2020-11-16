$("#id_regions").change(function () {
      var url = $("#testForm").attr("data-streets-url");
      var regionId = $(this).val();

      $.ajax({
        url: url,
        data: {
          'region': regionId
        },
        success: function (data) {
          $("#id_streets").html(data);
        }
      });

    });



    document.getElementById('id_home').placeholder = 'Дом';
    document.getElementById('id_flat').placeholder = 'Квартира';
    document.getElementById('id_phone').placeholder = 'Телефон';
    document.getElementById('id_tps_id').placeholder = 'TPS_ID';
    document.getElementById('id_street_only').placeholder = 'Альтернативная улица';
    document.getElementById('id_id').placeholder = 'Id заявки';
    document.querySelector('label[for="id_id"]').hidden=true;




