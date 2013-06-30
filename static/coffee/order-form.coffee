$(document).ready () ->
    $form = $('#order-form')

    $form.submit (e) ->
        e.preventDefault()

        data =
            address: $('#id_address').val()
            name: $('#id_name').val()
            email: $('#id_email').val()
        console.log data
        $.ajax
            type: 'POST'
            url: Django.url 'order_make'
            data: data
            success: (data, textStatus, jqXHR) ->
                # jqXHR.status 200 201
                console.log data
