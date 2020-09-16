let ajaxCommentShow = $('#ajxa-comment-show');

$('#comment-submit').click(function () {
    let content = $('#comment-content').val();
    let csrfToken = $('#django-csrf-token').val();
    let videoId = $(this).attr('data-video-id');
    let userId = $(this).attr('data-user-id');
    let url = $(this).attr('data-url');


    if (!content) {
        alert('评论不能为空!!!');
        return
    }

    $.ajax({
        url: url,
        data: {
            csrfmiddlewaretoken: csrfToken,
            content: content,
            videoId: videoId,
            userId: userId,
        },
        type: 'post',
        success: function (data) {
            if (data.code === 0) {
                ajaxCommentShow.html('');
                var _data = data.data.comment;
                var content = _data.comment;
                var username = _data.username;
                var str = content + ' ' + username;
                ajaxCommentShow.html(str);
                console.log(_data)
                // ajaxCommentShow.val(data.data)
            }
        },
        fail: function (e) {
            console.log(e, 11111);
        }


    });
});