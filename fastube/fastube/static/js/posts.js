$(document).ready(function() {
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

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
                var commentContent = comment.content + ' : posted by ' + comment.username;

                var commentListElement = $('<li>').text(commentContent);
                $('.comments-list').append(commentListElement);
            });
        },
        error: function(data) {
        },
    })

    commentsCreateFormElement.submit(function() {
        var content = $(commentsCreateFormInputContentElement).val();
        var data = {
            content: content,
        }

        $.ajax({
            url: commentAPIURL,
            type: 'POST',
            data: data,
            success: function(data) {

                // add comment
                var commentContent = data.content + ' : posted by ' + data.username;
                var newCommentList = $('<li>').text(commentContent);
                $('.comments-list').append(newCommentList);

                // update comment count
                var commentCount = $('#comments-count').html();
                var newCommentCount = Number(commentCount) + 1;
                $('#comments-count').html(String(newCommentCount));

                $(commentsCreateFormInputContentElement).val('');

            },
            error: function(data) {},
        })

        // TODO: Need to craft comment append function

        return false;
    });
});
