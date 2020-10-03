// 期間フィルタボタンが押されたときの処理
$('input[name="period_type"]').on("change", function () {
  label = $('label[for="' + this.id + '"]');
  posters = $('div[class="poster"][name="' + this.value + '"]');
  if ($(this).prop("checked")) {
    label.addClass("active");
    posters.each(function (i, elm) {
      $(elm).parent().show("fast");
    });
  } else {
    label.removeClass("active");
    posters.each(function (i, elm) {
      $(elm).parent().hide("fast");
    });
  }
});