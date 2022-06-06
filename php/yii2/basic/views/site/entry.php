<?php
namespace app\controllers;

use Yii;
use yii\web\Controller;
use app\models\EntryForm;

class SiteController extends Controller{
    public function actionEntry(){
        $model = new EntryForm();
        if($model->load(Yii::$app->request->post()) && $model->validate()){
            return $this->render('entry-confirm', ['model' => $model]);
        }else{
            return $this->render('entry', ['model' => $model]);
        }
    }

    
}


?>