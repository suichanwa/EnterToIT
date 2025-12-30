document.addEventListener('DOMContentLoaded', () => {
    resizeIcons();
    dragNDrop();
});

function resizeIcons() {
    const icons = document.querySelectorAll('.icons img');

    icons.forEach(icon => {
        icon.style.width = '64px';
        icon.style.height = '64px';
    });
}


function dragNDrop(){
    const $icons = $('.icons img');
    const $slots = $('.free-slots .slot');
    let $dragged = null;

    $icons.attr('draggable', true)
        .on('dragstart', function(e) {
            $dragged = $(this);
            try { e.originalEvent.dataTransfer.setData('text/plain', ''); } catch (err) {}
            setTimeout(() => {
                $dragged.css('display', 'none');
            }, 0);
        })
        .on('dragend', function(e) {
            setTimeout(() => {
                $(this).css('display', 'block');
                $dragged = null;
            }, 0);
        });

    $slots.on('dragover', function(e) {
        e.preventDefault();
        $(this).addClass('hovered');
    }).on('dragleave', function() {
        $(this).removeClass('hovered');
    }).on('drop', function(e) {
        e.preventDefault();
        $(this).removeClass('hovered');
        if ($dragged) {
            $(this).append($dragged);
        }
    });

    $('.icons').on('dragover', function(e) {
        e.preventDefault();
        $(this).addClass('hovered');
    }).on('dragleave', function() {
        $(this).removeClass('hovered');
    }).on('drop', function(e) {
        e.preventDefault();
        $(this).removeClass('hovered');
        if ($dragged) {
            $(this).append($dragged);
        }
    });
}