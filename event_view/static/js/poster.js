marked.setOptions({ breaks: true });
const renderMarkdown = function () {
  $(".event-content").each(function (index, elm) {
    $(elm).html(marked($(elm).text()));
  });
};
$(function () {
  renderMarkdown();
});
