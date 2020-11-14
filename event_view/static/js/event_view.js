// 期間フィルタボタンが押されたときの処理
$('input[name="period_type"]').on("change", function () {
  // ボタンに対応するラベルを取得
  label = $('label[for="' + this.id + '"]');
  // 各イベントの poster を取得
  posters = $('div[class="poster"][name="' + this.value + '"]');
  // ラジオボタンがチェックされていればボタンをactiveにして、ポスターを表示させる
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
// modal
// modal open
$("#info_btn").on("click", function () {
  $("#updateInfoModal").modal("show");
  updatePreview("#markdown_edit");
});
// テキストエリアの値をmarkdown表示にする
let updatePreview = function (elm) {
  if (!$(elm).val()) {
    return;
  }
  let html = marked($(elm).val());
  $("#update-info").html(html);
};
// キー入力がされた際にmarkdown表示を更新
$(function () {
  $("#markdown_edit").keyup(function () {
    updatePreview(this);
  });
  updatePreview($("#markdwon_edit"));
});
// info編集エディタ
// 初期は非表示に
$("#update-info-editor").hide();
$("#editor-save-btn").hide();
//表示切り替え
$("#editor-toggle-btn").on("click", function () {
  $("#update-info-editor").toggle();
  $("#editor-save-btn").toggle();
});
