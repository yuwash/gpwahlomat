var app = angular.module('myApp', ['ngRoute']);

// ------------- Route -----------
app.config(function($routeProvider) {
  $routeProvider
  .when('/', {
    templateUrl : 'pages/start.html'
  })
  .when('/result', {
    templateUrl : 'pages/result.html'
  })
  .when('/questions', {
    templateUrl : 'pages/questions.html'
  })
  .when('/favorites', {
    templateUrl : 'pages/favorites.html'
  })
  .otherwise({redirectTo: '/'});
});

// --------- Factory ---------

angular.module('myApp').factory('Data', function($http,$routeParams){
  
  var getData = function(){
    return $http({method:"GET", url:"extpages/externalJSON.json"})
    .then(function(extern) {
      return extern.data;
    });
  }
  return { getData: getData };
});

// ---------- Loading function ------------

function myFunction($scope, Data) { 
    var myDataPromise = Data.getData(); 
    myDataPromise.then(function(result) {
      if($scope.data == undefined){
        $scope.data = result;
      }
      console.log($scope.data); 
    }); 
 }

// --------- Main --------

app.controller('MainCtrl', function($scope, $http, Data, $rootScope,$routeParams){
  
  $scope.question_nr = 0;
  $scope.title1 = "Startseite";
  $scope.wasLastQuestion = false;
  $scope.visibleParty = null;

  // load Data
  myFunction($scope, Data);
  $scope.isLastQuestion = function() {
    return $scope.wasLastQuestion; 
  }
  $scope.correct = function() {
    $scope.wasLastQuestion =false; 
  }
  $scope.forward  = function() {
    if($scope.question_nr<$scope.data.questions.length-1){
        $scope.question_nr = $scope.question_nr + 1;
    }else{
        $scope.wasLastQuestion = true;
    }
  }
    $scope.back = function() {
        if($scope.question_nr>0){
            $scope.question_nr=$scope.question_nr-1;
        }else{
            window.location.href = "#/start";
        }
    }
    $scope.vote = function(rating) {
      $scope.data.questions[$scope.question_nr].answer=rating;
    }
    $scope.getFav = function(isFav){
      if(isFav) return "fa fa-star";
      return "fa fa-star-o";
    }
    $scope.getRating = function(rating){
      if(rating == 1)return "positive";
      if(rating == -1)return "negative";
      return "neutral";
    }
    $scope.toggle = function(partyid){

    }
    $scope.getTotalPosition = function(id){
      var tmp=0;
      for(var i=0; i<$scope.data.questions.length; i++){
        var u_rating = $scope.data.questions[i].answer*(1+$scope.data.questions[i].accent);
        tmp+=u_rating * $scope.data.questions[i].positions[id].orientation;
      }
      return tmp*10;
    }
    $scope.setPartyVisible = function(id){
      if(id == $scope.visibleParty){
        $scope.visibleParty = null;
      }else{
        $scope.visibleParty = id;
      }
    }
    $scope.isPartyVisible = function(id){
      return id == $scope.visibleParty;
    }
});