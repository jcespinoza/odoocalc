# Ngcalc

The client side of the Odoo Calc module.

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 8.0.3.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

To test the client in solation it might be useful to fire up the fake API server with `npm run fake` which will respond at `http://localhost:8069`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

Run `npm build-prod` to build the project for Odoo. The build artifacts will be stored in the `../static/src/` directory. They will have no hashing for easier deployments, the downside being clients need to hard refresh the cache after updates.

## Running unit tests (Not intended to pass)

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests (not intended to pass)

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

Integration with Odoo based on the guidance provided on [this video:](https://www.youtube.com/watch?v=qNNCEGIiySE)

