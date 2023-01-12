odoo.define("pos_required.ClientDetailsEdit", function (require) { // odoo.define("ModuleName.FileName/DesiredName",function(require)
    "use strict";

    const { _t } = require('web.core');
    const Registries = require("point_of_sale.Registries");
    var ClientDetailsEdit = require("point_of_sale.ClientDetailsEdit"); // var VaraibleName1 = require("InheritModuleName.InheritClassName");
    // VariableName1 same as InheritClassName

    var ClientDetailsEditInherit = (ClientDetailsEdit) => // var VaraibleName2 = (VaraibleName1) => Arrow function
        class extends ClientDetailsEdit { // class extends InheritClassName
            savesChanges() { // BaseFunctionToInherit()
                let processedChanges = {};
                for (let [key, value] of Object.entries(this.changes)) {
                    if (this.intFields.includes(key)) {
                        processedChanges[key] = parseInt(value) || false;
                    } else {
                        processedChanges[key] = value;
                    }
                }
                if ((!this.props.partner.name && !processedChanges.name) ||
                    processedChanges.name === '') {
                    return this.showPopup('ErrorPopup', {
                        title: _t(' Name Is Required'),
                    });
                }
                if ((!this.props.partner.phone && !processedChanges.name) ||
                    processedChanges.name === '') {
                    return this.showPopup('ErrorPopup', {
                        title: _t(' Phone Is Required'),
                    });
                }
                if ((!this.props.partner.vat && !processedChanges.name) ||
                    processedChanges.name === '') {
                    return this.showPopup('ErrorPopup', {
                        title: _t(' Tax ID Is Required'),
                    });
                }
                processedChanges.id = this.props.partner.id || false;
                this.trigger('save-changes', { processedChanges });

            }

        };

    Registries.Component.extend(ClientDetailsEdit, ClientDetailsEditInherit); // Registries.Component.extend(VaraibleName1,VaraibleName2)
    return ClientDetailsEdit; // return VariableName1;
});