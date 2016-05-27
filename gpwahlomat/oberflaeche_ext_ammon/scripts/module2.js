var app = angular.module('myApp', ['ngRoute']);
console.log("TEST");

app.config(function($routeProvider) {
  $routeProvider
  .when('/', {
    templateUrl : 'pages/start.html',
    controller  : 'StartCtrl'
  })
  .when('/questions', {
    templateUrl : 'pages/questions.html',
    controller  : 'QuestionCtrl'
  })
  .when('/favorites', {
    templateUrl : 'pages/favorites.html',
    controller  : 'FavoritesCtrl'
  })
  .when('/result', {
    templateUrl : 'pages/result.html',
    controller  : 'ResultCtrl'
  })
  .otherwise({redirectTo: '/'});
});

app.controller('StartCtrl', function($scope) {
  console.log("TTTTT");
  $scope.message = 'Hello from HomeController';
});
app.controller('QuestionCtrl', function($scope) {
  $scope.message = 'Hello from AboutController';
});
app.controller('FavoritesCtrl', function($scope) {
  $scope.message = 'Hello from HomeController';
});
app.controller('ResultCtrl', function($scope) {
  $scope.message = 'Hello from AboutController';
});