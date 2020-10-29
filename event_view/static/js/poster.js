marked.setOptions({ breaks: true });
$(function () {
  $(".event-content").each(function (index, elm) {
    $(elm).html(marked($(elm).text()));
  });
});
