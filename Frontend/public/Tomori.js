mdui.mutation();

function selectDirectory() {
    window.pywebview.api.select_directory().then(function (directory) {
        document.getElementById('directory').value = directory;
    });
}

function openTool(toolFunction) {
    toolFunction().then(function (result) {
        alert(result);
    }).catch(function (error) {
        alert('发生错误: ' + error,);
    });
}

function openGames() {
    openTool(window.pywebview.api.OpenGames);
}
