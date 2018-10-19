(function(){
  'use strict';

  var routePrefix = '/static/app/';

  // Setup the routes for the 'mwachx' module
  angular.module('mwachx')
    .config(['$stateProvider', '$urlRouterProvider',
      function($stateProvider, $urlRouterProvider) {

        // Redirect to home in case we get lost
        $urlRouterProvider.otherwise('/');

        $stateProvider
          .state('home', {
            url:          '/',
            templateUrl:  routePrefix + 'dashboard/home.html',
            controller:   'HomeController'
          })

          // Participant state and substates
          .state('participant-list', {
            url:          '/participant?message',
            templateUrl:  routePrefix + 'dashboard/participant/participantList.html',
            controller:   'ParticipantListController'
          })

          .state('participant-new', {
            url:          '/participant/new',
            templateUrl:   'crispy-forms/participant/new',
            // controller:   'ParticipantNewController'
          })
          .state('participant-details', {
            url:          '/participant/:study_id',
            templateUrl: routePrefix  + 'participantDetail/participantDetail.html',
            controller:  'ParticipantController'
          })

          // Message state and substates
          .state('pending-messages', {
            url: '/pending/messages',
            templateUrl: routePrefix + 'dashboard/messages/pendingMessages.html',
            controller: 'PendingMessageController'
          })

          // Visit state and substates
          .state('pending-visits', {
            url: '/pending/visits',
            templateUrl: routePrefix + 'dashboard/visits/pendingVisits.html',
            controller: 'PendingVisitsController'
          })

          // Upcoming Visits state and substates
          .state('visits-upcoming', {
            url: '/vists/upcoming',
            templateUrl: routePrefix + 'dashboard/visits/upcomingVisits.html',
            controller: 'UpcomingVisitsController'
          })

          // Calls state and substates
          .state('pending-calls',{
            url: '/pending/calls',
            templateUrl: routePrefix + 'dashboard/calls/calls.html',
            controller: 'UpcomingCallsController',
          })

          // Translation state and substates
          .state('translations', {
            url: '/translations/',
            templateUrl: routePrefix + 'dashboard/translations/pendingTranslations.html',
            controller: 'PendingTranslationController',
          })

      }]);


  // *************************************
  // Basic Controller For Test Route
  // *************************************

  angular.module('mwachx')
    .controller('TestController',['$scope',
      function ($scope) {
        $scope.status = {art_initiation:false}
      }]);

})();
