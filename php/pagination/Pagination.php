<?php
class Pagination {
    public int $count_page = 1;
    public int $current_pages = 1;
    public string $url = '';
    public int $mid_size = 5;
    public int $end_size = 10;

    public function __construct(
        public int $page = 1,
        public int $per_pag = 1,
        public int $total = 1,
    ){
        $this->count_page = ceil($total / $per_pag);
        $this->current_pages = $this->get_current_pages($page);
    }

    public function get_count_pages(){
        return $this->count_page; 
    }

    public function get_current_pages(){
        if($this->page > $this->count_page){
            $this->page = $this->count_page;
        }

        if($this->page < 1){
            $this->page = 1;
        }
    }
}
?>