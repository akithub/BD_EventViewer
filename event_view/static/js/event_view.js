// 期間フィルタボタンが押されたらactiveになるように
$('input[name="period_type"]').on("change", function () {
  label = $('label[for="' + this.id + '"]');
  if ($(this).prop("checked")) {
    label.addClass("active");
  } else {
    label.removeClass("active");
  }
});
