setContentHeight = () ->
    $content = $('#content')

    setMainHeight = () ->
        height = $(window).height() - $('#menu').outerHeight() -  $('#footer').outerHeight()
        $content.height height
        $content.find('.span12').height height

    setMainHeight()

    $(window).resize () ->
        setMainHeight()

yaCounterHit = (url, title, refer) ->
    if sessionStorage.dontHitMetrica
        return

    console.debug 'Hit metrika', url, title, refer
    try
        yaCounter9374383.hit url, title, refer
    catch error
        console.error 'Hit the metrika', error