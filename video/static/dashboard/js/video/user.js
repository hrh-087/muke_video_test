$(".user-status-submit").click(function () {
    let url = $(this).attr('data-url');
    let userId = $(this).attr('data-user-id');
    let csrfToken = $('#django-csrf-token').val();

    console.log(url,userId,csrfToken);
    $.ajax({
        url: url,
        data: {
            userId: userId,
            csrfmiddlewaretoken: csrfToken,
        },
        type: 'post',
        success: function (data) {
            if (data.code === 0) {
                alert(data.msg);
                window.location.href = window.location.href;
            } else {
                alert(data.msg)
            }
        },
        fail: function (e) {
            console.log(e)
        }

    })


});