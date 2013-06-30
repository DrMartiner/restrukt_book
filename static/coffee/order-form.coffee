$(document).ready () ->
    $form = $('#order_form')

    $form.submit (e) ->
        e.preventDefault()

        data =
            address: $('#id_address').val()
            name: $('#id_name').val()
            email: $('#id_email').val()
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()

        $.ajax
            type: 'POST'
            url: Django.url 'order_make'
            data: data
            beforeSend: (jqXHR, settings) ->
                $('#loader').show()
                $form.find('.control-group').each () ->
                    $(@).removeClass 'error'
                    $(@).find('.help-inline').text ''

            success: (data, textStatus, jqXHR) ->
                switch jqXHR.status
                    when 200
                        $('#loader').hide()
                        for name of data
                            $field = $('#id_' + name).parents('.control-group')
                            $field.addClass 'error'
                            $field.find('.help-inline').text data[name]
                    when 201
                        $('#id_xml').val data.xml
                        $('#id_sign').val data.sign
                        $('#payment_form').submit()