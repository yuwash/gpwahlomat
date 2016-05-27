var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {
    
    $http.get("externalJson/external.html")
    .then(function(extern) {
        $scope.categories = extern.data.categories;
        $scope.questions = extern.data.questions;
        $scope.tenor = extern.data.tenor;
        $scope.parties = extern.data.parties;
    },function(questions){
    });
    $scope.resetJson  = function() {
        for(i = 0; i < $scope.questions.length; i++){
            $scope.questions[i].answer=null;
        }
    }
    $scope.fillJson  = function() {
        for(i = 0; i < $scope.questions.length; i++){
            if($scope.questions[i].answer==null){
                $scope.questions[i].answer=0;
            }
            
        }
    }
    $scope.forward  = function() {
        if($scope.question_nr<$scope.questions.length-1){
            $scope.question_nr = $scope.question_nr + 1;
        }else{
            $scope.fillJson();
            $scope.page_nr = $scope.page_nr + 1;
        }
    }
    $scope.back = function() {
        if($scope.question_nr>0){
            $scope.question_nr=$scope.question_nr-1;
        }else{
            $scope.page_nr = 0;
            $scope.resetJson();//reset
        }
    }
    $scope.vote = function(rating) {
        $scope.questions[$scope.question_nr].answer=rating;
    }
    $scope.getClassFromRating = function(rating) {
        if(rating == 0){
            return "neutral";
        }else if(rating == 1){
            return "positive";
        }else if(rating == -1){
            return "negative";
        }
        return null;
    }
    $scope.getClassFromFavorite = function(fav) {
        if(fav){
            return "fav";
        }else{
            return "nofav";
        }
        return null;
    }
    $scope.getFavoriteStar = function(fav) {
        if(fav){
            return "images/Starfav.png";
        }else{
            return "images/Starnofav.png";
        }
        return null;
    }
    $scope.getConformity = function(party) {
        var value=0;
        for(i = 0; i < $scope.questions.length; i++){
            value = value + parseInt($scope.questions[i].answer) * parseInt($scope.questions[i].positions[party].orientation);
        }
        return 100*((value+1)/$scope.questions.length);
    }
});