$('#regist-submit').click(function () {
    let username = $('#username').val();
    let password = $('#password').val();
    let url = $(this).attr('data-url');
    let csrfToken = $('#django-csrf-token').val();

    if (!username || !password) {
        alert('缺少必要字段');
        return;
    }

    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password,
            csrfmiddlewaretoken: csrfToken
        },
        success: function (data) {
            alert(data.msg)
        },
        fail: function (e) {
            console.log('error:%s', e)
        }
    })
});

$('#login-submit').click(function () {
    let username = $('#username').val();
    let password = $('#password').val();
    let url = $(this).attr('data-url');
    let csrfToken = $('#django-csrf-token').val();

    if (!username || !password) {
        alert('缺少必要字段');
        return;
    }

    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password,
            csrfmiddlewaretoken: csrfToken
        },
        success: function (data) {
            if (data.code) {
                alert(data.msg)
            } else {
                window.location.href = '/client/video/ex';
            }
        },
        fail: function (e) {
            console.log('error:%s', e)
        }
    })
});