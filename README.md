
<h1 align="center">
  Street Harassment Proyect - Data Structures and Algorithms I
  <br>
</h1>

<h4> Team members: Lina Ballesteros and Camilo Córdoba
  <br>
  </h1>
</p>
</p>

![image](https://user-images.githubusercontent.com/103126242/200477431-9acc2e45-baee-48e7-8504-76682bd10060.png)


# Third Delivery Update 
## Code 
* Program can now receive custom coordinates and verify if the given coords are in the dataframe of the streets of Medellín.
  - Check out `customizeCoords()` at the "backmethods" file.
* Program shows 3 paths by redefining the variable v in 3 different ways with Dijkstra's Algorithm.
  - Red path: `v = l * r`
  - Green path: `v = l**(2*r)`
  - Purple path: `v = l + (80r)`
* Added `getDistanceOfPath()` at the "backmethods" file which give us the total length and average risk of a path.
  - Function is being called 3 times to see all the results for each path. 

### Technical Report and Slides

Both technical report and for this delivery have been added to the third delivery folder

## How does this Proyect work ?

Code files are divided in 3 files: 

* [backmethods.py](https://github.com/linasofi13/StreetHarassmentProyect_2022-2/blob/master/codigo/backmethods.py)

  - This file contains all the methods we call in the main file, some of them are:

`generateGraph()`
`getCoords()`
`dijkstraShortestSafest()`

* [main.py](https://github.com/linasofi13/StreetHarassmentProyect_2022-2/blob/master/codigo/main.py)

  - This is the executable file, here we have the main menu inside an infinite loop, which offers us different places to test the algorithm
  or we can just add the coords that we want to test. You can also quit the program by entering the specific option in the menu. 
  - We keep calling functions from backmethods.py. and path_map.py.

* [path_map.py](https://github.com/linasofi13/StreetHarassmentProyect_2022-2/blob/master/codigo/path_map.py)

  - This is our file to draw. We use "Folium", a really nice library to draw the 3 paths requested and we added cute markers to the starting point and the destination.

<h1 align="center"> GitPoint </h1> <br>
<p align="center">
  <a href="https://gitpoint.co/">
    <img alt="GitPoint" title="GitPoint" src="http://i.imgur.com/VShxJHs.png" width="450">
  </a>
</p>

<p align="center">
  GitHub in your pocket. Built with React Native.
</p>

<p align="center">
  <a href="https://itunes.apple.com/us/app/gitpoint/id1251245162?mt=8">
    <img alt="Download on the App Store" title="App Store" src="http://i.imgur.com/0n2zqHD.png" width="140">
  </a>

  <a href="https://play.google.com/store/apps/details?id=com.gitpoint">
    <img alt="Get it on Google Play" title="Google Play" src="http://i.imgur.com/mtGRPuM.png" width="140">
  </a>
</p>

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Feedback](#feedback)
- [Contributors](#contributors)
- [Build Process](#build-process)
- [Backers](#backers-)
- [Sponsors](#sponsors-)
- [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

[![Build Status](https://img.shields.io/travis/gitpoint/git-point.svg?style=flat-square)](https://travis-ci.org/gitpoint/git-point)
[![Coveralls](https://img.shields.io/coveralls/github/gitpoint/git-point.svg?style=flat-square)](https://coveralls.io/github/gitpoint/git-point)
[![All Contributors](https://img.shields.io/badge/all_contributors-73-orange.svg?style=flat-square)](./CONTRIBUTORS.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg?style=flat-square)](http://commitizen.github.io/cz-cli/)
[![Gitter chat](https://img.shields.io/badge/chat-on_gitter-008080.svg?style=flat-square)](https://gitter.im/git-point)

View repository and user information, control your notifications and even manage your issues and pull requests. Built with React Native, GitPoint is one of the most feature-rich unofficial GitHub clients that is 100% free.

**Available for both iOS and Android.**

<p align="center">
  <img src = "http://i.imgur.com/HowF6aM.png" width=350>
</p>

## Features

A few of the things you can do with GitPoint:

* View user activity feed
* Communicate on your issue and pull request conversations
* Close or lock issues
* Apply labels and assignees
* Review and merge pull requests
* Create new issues
* Star, watch and fork repositories
* Control your unread and participating notifications
* Easily search for any user or repository

<p align="center">
  <img src = "http://i.imgur.com/IkSnFRL.png" width=700>
</p>

<p align="center">
  <img src = "http://i.imgur.com/0iorG20.png" width=700>
</p>

## Feedback

Feel free to send us feedback on [Twitter](https://twitter.com/gitpointapp) or [file an issue](https://github.com/gitpoint/git-point/issues/new). Feature requests are always welcome. If you wish to contribute, please take a quick look at the [guidelines](./CONTRIBUTING.md)!

If there's anything you'd like to chat about, please feel free to join our [Gitter chat](https://gitter.im/git-point)!

## Contributors

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification and is brought to you by these [awesome contributors](./CONTRIBUTORS.md).

## Build Process

- Follow the [React Native Guide](https://facebook.github.io/react-native/docs/getting-started.html) for getting started building a project with native code. **A Mac is required if you wish to develop for iOS.**
- Clone or download the repo
- `yarn` to install dependencies
- `yarn run link` to link react-native dependencies
- `yarn start:ios` to start the packager and run the app in the iOS simulator (`yarn start:ios:logger` will boot the application with [redux-logger](<https://github.com/evgenyrodionov/redux-logger>))
- `yarn start:android` to start the packager and run the app in the the Android device/emulator (`yarn start:android:logger` will boot the application with [redux-logger](https://github.com/evgenyrodionov/redux-logger))

Please take a look at the [contributing guidelines](./CONTRIBUTING.md) for a detailed process on how to build your application as well as troubleshooting information.

**Development Keys**: The `CLIENT_ID` and `CLIENT_SECRET` in `api/index.js` are for development purposes and do not represent the actual application keys. Feel free to use them or use a new set of keys by creating an [OAuth application](https://github.com/settings/applications/new) of your own. Set the "Authorization callback URL" to `gitpoint://welcome`.

## Backers [![Backers on Open Collective](https://opencollective.com/git-point/backers/badge.svg)](#backers)

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/git-point#backer)]

<a href="https://opencollective.com/git-point#backers" target="_blank"><img src="https://opencollective.com/git-point/backers.svg?width=890"></a>

## Sponsors [![Sponsors on Open Collective](https://opencollective.com/git-point/sponsors/badge.svg)](#sponsors)

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/git-point#sponsor)]

<a href="https://opencollective.com/git-point/sponsor/0/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/1/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/2/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/3/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/4/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/5/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/6/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/7/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/8/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/9/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/9/avatar.svg"></a>

## Acknowledgments

Thanks to [JetBrains](https://www.jetbrains.com) for supporting us with a [free Open Source License](https://www.jetbrains.com/buy/opensource).
