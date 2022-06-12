<?php
namespace core;


class View{
    public function RenderPage(Page $page){
        return $this->renderLayout($page, $this->renderView($page));
    }

    private function renderLayout(Page $page, $content){
        $layoutPath = $_SERVER['DOCUMENT_ROOT'] . 'views/' . $page->layout;

        if(file_exists($layoutPath)){
            ob_start();
            include $layoutPath;
            return ob_get_clean();
        }
    }
    
    private function renderView(Page $page){
        $viewPath = $_SERVER['DOCUMENT_ROOT'] . 'views/' . $page->view . '.php';
        if(file_exists($viewPath)){
            ob_start();
            include $viewPath;
            return ob_get_clean();
        }
    }

}


?>