# OdooCalc
A calculator module for Odoo 11

Written in response to a challenge from @jimmybanegas93

## Development
- Install dependencies of the Angular app located in the `./ngcalc` subdirectory.
- Run `npm run build-prod` to build bundles and copy them to the `satic` folder of  Odoo module.

### Unit test
- Tests are `unittest` tests and work out of the box under Linux as long as Odoo python libraries are added to sys.path

## Installation
- Install `Base Instal Module` from the Apps list in Odoo
- Add to the addons folder on the target machine. Can't be installed from the UI as a .zip since it has python code.
- Addons must be located in its own subfolder in `addons` so that every subdirectory has a `__init__.py`
- Make sure to hard refresh the browser during updates to Angular app