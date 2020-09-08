$('#comment-submit').click(function () {
    let content = $('#comment-content').val();
    let csrfToken = $('#django-csrf-token').val();
    let videoId = $(this).attr('data-video-id');
    let userId = $(this).attr('data-user-id');
    let url = $(this).attr('data-url');

    if (!content) {
        alert('评论不能为空!!!')
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
        success:function (data) {
            console.log(data);
        },
        fail:function (e) {
            console.log(e,11111);
        }
        
        

    });
    console.log(videoId, userId)
});