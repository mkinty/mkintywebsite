const modal = document.getElementById("modal");
const dialog = document.getElementById("dialog");

const CKEDITOR_CONFIG = {
    toolbar: [
        'heading', '|',
        'bold', 'italic', 'underline', 'strikethrough', 'code', '|',
        'link', 'bulletedList', 'numberedList', '|',
        'outdent', 'indent', '|',
        'subscript', 'superscript', 'removeFormat', '|',
        'blockQuote', 'codeBlock', 'sourceEditing', '|',
        'fontFamily', 'fontSize', 'alignment', '|',
        'imageUpload', 'mediaEmbed', 'insertTable', '|',
        'undo', 'redo'
    ],
    image: {
        toolbar: [
            'imageStyle:full',
            'imageStyle:side',
            '|',
            'imageTextAlternative'
        ]
    }
};

// Fonction pour initialiser CKEditor sur tous les textareas injectés
function initCKEditorOnInjectedTextareas(container) {
    container.querySelectorAll("textarea.django_ckeditor_5").forEach(el => {
        // Vérifie si l'éditeur n'est pas déjà initialisé
        if (!el.classList.contains("ck-editor__editable")) {
            ClassicEditor
                .create(el, CKEDITOR_CONFIG)
                .then(editor => {
                    // Optionnel : on peut stocker l'instance sur l'élément si besoin
                    el._ckeditorInstance = editor;
                })
                .catch(error => console.error(error));
        }
    });
}

// Quand HTMX injecte le contenu dans le modal
htmx.on("htmx:afterSwap", (e) => {
    if (e.detail.target.id === "dialog") {
        modal.classList.remove("hidden");

        const firstChildId = e.detail.target.firstElementChild?.id;

        dialog.classList.remove("small", "medium", "large");
        if (firstChildId === "small") {
            dialog.classList.add("small");
        } else if (firstChildId === "medium") {
            dialog.classList.add("medium");
        } else if (firstChildId === "large") {
            dialog.classList.add("large");
        }

        // 🔥 Initialiser CKEditor sur le textarea injecté
        initCKEditorOnInjectedTextareas(e.detail.target);
    }
});

// Fermer le modal si on clique en dehors du dialogue
modal.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.classList.add("hidden");

        // Détruit les instances CKEditor avant de vider le contenu
        dialog.querySelectorAll("textarea.django_ckeditor_5").forEach(el => {
            if (el._ckeditorInstance) {
                el._ckeditorInstance.destroy();
                el._ckeditorInstance = null;
            }
        });

        dialog.innerHTML = ""; // vider le contenu
    }
});