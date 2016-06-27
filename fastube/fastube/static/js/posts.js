$(document).ready(function() {
    var commentsSectionElement = $('#comments-section');
    var commentsCreateFormElement = $(commentsSectionElement).find('form');
    var commentsCreateFormInputContentElement = $(commentsCreateFormElement).find('input[name="content"]');

    var postSlug = $('#comments-count').data('post-slug');
    var commentAPIURL = '/api/posts/' + postSlug + '/comments/';

    $.ajax({
        url: commentAPIURL,
        type: 'GET',
        success: function(data) {
            var commentsCount = data.length;
            $('#comments-count').html(commentsCount);

            data.forEach(function(comment) {
                var commentContent = comment.content + ': posted by ' + comment.username;

                var commentListElement = $('<li>').text(commentContent);
                $('.comments-list').append(commentListElement);
            });
        },
        error: function(data) {
        },
    })

    commentsCreateFormElement.submit(function() {
        var content = $(commentsCreateFormInputContentElement).val();
        alert(commentAPIURL);
        $(commentsCreateFormInputContentElement).val('')

        return false;
    });
});
