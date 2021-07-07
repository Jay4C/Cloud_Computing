import unittest
import requests


class balance(unittest.TestCase):
    def test_GET_balances(self):
        print("test_GET_balances")

        # Parameters
        access_signature = ""
        access_tag = ""
        access_user_id = ""
        access_user_ip = ""
        wallet_id = ""
        user_id = ""

        url = "https://sandbox.treezor.com/v1/index.php/balances?" \
              + "accessSignature=" + access_signature \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip \
              + "&walletId=" + wallet_id \
              + "&userId=" + user_id

        payload = {}
        headers = {'Accept': 'application/json'}

        response = requests.request("GET", url, headers=headers, data=payload)

        # Response class
        print(response.text.encode('utf8'))


class bankaccount(unittest.TestCase):
    def test_GET_bankaccounts(self):
        print("test_GET_bankaccounts")

        # parameters
        access_signature = ""
        access_tag = ""
        access_user_id = ""
        access_user_ip = ""
        bankaccount_id = ""
        bankaccount_status = ""
        user_id = ""
        bankaccount_iban = ""
        page_number = ""
        page_count = ""
        sort_by = ""
        sort_order = ""
        created_date_from = ""
        created_date_to = ""
        updated_date_from = ""
        updated_date_to = ""

        url = "https://sandbox.treezor.com/v1/index.php/bankaccounts?" \
              + "accessSignature=" + access_signature \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip \
              + "&bankaccountId=" + bankaccount_id \
              + "&bankaccountStatus=" + bankaccount_status \
              + "&userId=" + user_id \
              + "&bankaccountIBAN=" + bankaccount_iban \
              + "&pageNumber=" + page_number \
              + "&pageCount=" + page_count \
              + "&sortBy=" + sort_by \
              + "&sortOrder=" + sort_order \
              + "&createdDateFrom=" + created_date_from \
              + "&createdDateTo=" + created_date_to \
              + "&updatedDateFrom=" + updated_date_from \
              + "&updatedDateTo=" + updated_date_to

        payload = {}
        headers = {'Accept': 'application/json'}

        response = requests.request("GET", url, headers=headers, data=payload)

        # Response class
        print(response.text.encode('utf8'))

    def test_POST_bankaccounts(self):
        print("test_POST_bankaccounts")

        # Parameters
        access_signature = ""
        access_tag = ""
        access_user_id = ""
        access_user_ip = ""
        bankaccount_tag = ""
        user_id = ""
        name = ""
        bankaccount_owner_name = ""
        bankaccount_owner_address = ""
        bankaccount_iban = ""
        bankaccount_bic = ""
        bankaccount_type = ""

        url = "https://sandbox.treezor.com/v1/index.php/bankaccounts?" \
              + "accessSignature=" + access_signature \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip \
              + "&bankaccountTag=" + bankaccount_tag \
              + "&userId=" + user_id \
              + "&name=" + name \
              + "&bankaccountOwnerName=" + bankaccount_owner_name \
              + "&bankaccountOwnerAddress=" + bankaccount_owner_address \
              + "&bankaccountIBAN=" + bankaccount_iban \
              + "&bankaccountBIC=" + bankaccount_bic \
              + "&bankaccountType=" + bankaccount_type

        payload = {}
        headers = {'Accept': 'application/json'}

        response = requests.request("POST", url, headers=headers, data=payload)

        # Response class
        print(response.text.encode('utf8'))

    def test_DELETE_bankaccounts(self):
        print("test_DELETE_bankaccounts")

        # Parameters
        id = 11

        url = "https://sandbox.treezor.com/v1/index.php/bankaccounts/" + str(id)

        payload = {}
        headers = {'Accept': 'application/json'}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        # Response class
        print(response.text.encode('utf8'))

    def test_GET_bankaccounts(self):
        print("test_GET_bankaccounts")

        # Parameters
        id = 111

        url = "https://sandbox.treezor.com/v1/index.php/bankaccounts/" + str(id)

        payload = {}
        headers = {'Accept': 'application/json'}

        response = requests.request("GET", url, headers=headers, data=payload)

        # Response class
        print(response.text.encode('utf8'))


class beneficiairies(unittest.TestCase):
    def test_GET_beneficiaries(self):
        print("test_GET_beneficiaries")

        # Parameters
        access_signature = "access_signature"
        access_tag = "access_tag"
        access_user_id = "access_user_id"
        access_user_ip = "access_user_ip"
        fields = ["field_1", "field_2"]
        filter = "filter"
        id = "id"
        user_id = "user_id"
        iban = "iban"
        bic = "bic"
        nick_name = "nick_name"
        name = "name"
        page_number = "page_number"
        page_count = "page_count"
        sort_by = "sort_by"
        sort_order = "sort_order"

        url = "https://sandbox.treezor.com/v1/index.php/beneficiaries?" \
              + "accessSignature=" + access_signature \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip \
              + "&fields=" + fields \
              + "&filter=" + filter \
              + "&id=" + id \
              + "&userId=" + user_id \
              + "&iban=" + iban \
              + "&bic=" + bic \
              + "&nickName=" + nick_name \
              + "&name=" + name \
              + "&pageNumber=" + page_number\
              + "&pageCount=" + page_count \
              + "&sortBy=" + sort_by \
              + "&sortOrder=" + sort_order

        payload = {}
        headers = {'Accept': 'application/json'}

        response = requests.request("GET", url, headers=headers, data=payload)

        # response
        print(response.text.encode('utf8'))

    def test_POST_beneficiaries(self):
        print("test_POST_beneficiaries")

        # Parameters
        access_signature = "access_signature"
        access_tag = "access_tag"
        access_user_id = "access_user_id"
        access_user_ip = "access_user_ip"

        url = "https://sandbox.treezor.com/v1/index.php/beneficiaries?" \
              + "accessSignature=" + access_signature \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip

        payload = "{\r\n  \"tag\": \"string\",\r\n  \"userId\": 0,\r\n  \"nickName\": \"string\",\r\n  \"name\": \"string\",\r\n  \"address\": \"string\",\r\n  \"iban\": \"string\",\r\n  \"bic\": \"string\",\r\n  \"sepaCreditorIdentifier\": \"string\",\r\n  \"sddB2bWhitelist\": [\r\n    {\r\n      \"uniqueMandateReference\": \"string\",\r\n      \"isRecurrent\": true,\r\n      \"walletId\": 0\r\n    }\r\n  ],\r\n  \"sddCoreBlacklist\": [\r\n    \"string\"\r\n  ],\r\n  \"usableForSct\": false,\r\n  \"fields\": [\r\n    \"string\"\r\n  ]\r\n}"
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Response
        print(response.text.encode('utf8'))

    def test_GET_beneficiaries_id(self):
        print("test_GET_beneficiaries_id")

        # Parameters
        fields = "%5B%22field1%22%2C%20%22field2%22%5D"

        url = "https://sandbox.treezor.com/v1/index.php/beneficiaries/111?fields=" + fields

        payload = {}
        headers = {'Accept': 'application/json'}

        response = requests.request("GET", url, headers=headers, data=payload)

        # Response
        print(response.text.encode('utf8'))

    def test_PUT_beneficiaries_id(self):
        print("test_PUT_beneficiaries_id")

        # Parameters
        id = 111
        access_signature = "access_signature"
        access_tag = "access_tag"
        access_user_id = 111
        access_user_ip = "access_user_ip"

        url = "https://sandbox.treezor.com/v1/index.php/beneficiaries/" + str(id) + "?" \
              + "accessSignature=" + access_signature \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + str(access_user_id) \
              + "&accessUserIp=" + access_user_ip

        payload = "{\r\n  \"tag\": \"string\",\r\n  \"nickName\": \"string\",\r\n  \"name\": \"string\",\r\n  \"address\": \"string\",\r\n  \"iban\": \"string\",\r\n  \"bic\": \"string\",\r\n  \"sepaCreditorIdentifier\": \"string\",\r\n  \"sddB2bWhitelist\": [\r\n    {\r\n      \"uniqueMandateReference\": \"string\",\r\n      \"isRecurrent\": true,\r\n      \"walletId\": 0\r\n    }\r\n  ],\r\n  \"sddCoreBlacklist\": [\r\n    \"string\"\r\n  ],\r\n  \"usableForSct\": false,\r\n  \"fields\": [\r\n    \"string\"\r\n  ]\r\n}"
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        # Response
        print(response.text.encode('utf8'))


class business(unittest.TestCase):
    def test_GET_businesssearchs(self):
        print("test_GET_businesssearchs")

        # Parameters
        access_signature = "access_signature"
        access_tag = "access_tag"
        access_user_id = 11
        access_user_ip = "access_user_ip"
        country = "country"
        name_exact = "name_exact"
        name_match_beginning = "name_match_beginning"
        name_closest_keywords = "name_closest_keywords"
        registration_number = "registration_number"
        vat_number = "vat_number"
        phone_number = "phone_number"
        address_street = "address_street"
        address_city = "address_city"
        address_postal_code = "address_postal_code"

        url = "https://sandbox.treezor.com/v1/index.php/businesssearchs?" \
              + "accessSignature=" + access_signature \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + str(access_user_id) \
              + "&accessUserIp=" + access_user_ip \
              + "&country=" + country \
              + "&nameExact=" + name_exact \
              + "&nameMatchBeginning=" + name_match_beginning \
              + "&nameClosestKeywords=" + name_closest_keywords \
              + "&registrationNumber=" + registration_number \
              + "&vatNumber=" + vat_number \
              + "&phoneNumber=" + phone_number \
              + "&addressStreet=" + address_street \
              + "&addressCity=" + address_city \
              + "&addressPostalCode=" + address_postal_code

        payload = {}
        headers = {'Accept': 'application/json'}

        response = requests.request("GET", url, headers=headers, data=payload)

        # Response
        print(response.text.encode('utf8'))

    def test_GET_businessinformations(self):
        print("test_GET_businessinformations")

        # Parameters
        access_signature = "access_signature"
        access_tag = "access_tag"
        access_user_id = "access_user_id"
        access_user_ip = "access_user_ip"
        country = "country"
        registration_number = "registration_number"
        vat_number = "vat_number"
        external_id = "external_id"

        url = "https://sandbox.treezor.com/v1/index.php/businessinformations?" \
              + "accessSignature=" + access_signature \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip \
              + "&country=" + country \
              + "&registrationNumber=" + registration_number \
              + "&vatNumber=" + vat_number \
              + "&externalId=" + external_id

        payload = {}
        headers = {'Accept': 'application/json'}

        response = requests.request("GET", url, headers=headers, data=payload)

        # Response
        print(response.text.encode('utf8'))


class card(unittest.TestCase):
    def test_GET_cards(self):
        print("test_GET_cards")

        # Parameters
        access_signature = "access_signature"
        access_tag = "access_tag"
        access_user_id = "access_user_id"
        access_user_ip = "access_user_ip"
        card_id = "card_id"
        user_id = "user_id"
        embossed_name = "embossed_name"
        public_token = "public_token"
        perms_group = "perms_group"
        is_physical = "is_physical"
        is_converted = "is_converted"
        lock_status = "lock_status"
        mcc_restriction_group_id = "mcc_restriction_group_id"
        merchant_restriction_group_id = ""
        country_restriction_group_id = "country_restriction_group_id"
        page_number = "page_number"
        page_count = "page_count"
        sort_by = "sort_by"
        sort_order = "sort_order"
        created_date_from = "created_date_from"
        created_date_to = "created_date_to"
        updated_date_from = "updated_date_from"
        updated_date_to = "updated_date_to"

        url = "https://sandbox.treezor.com/v1/index.php/cards?" \
              + "accessSignature=" + access_signature \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip \
              + "&cardId=" + card_id \
              + "&userId=" + user_id \
              + "&embossedName=" + embossed_name \
              + "&publicToken=" + public_token \
              + "&permsGroup=" + perms_group \
              + "&isPhysical=" + is_physical \
              + "&isConverted=" + is_converted \
              + "&lockStatus=" + lock_status \
              + "&mccRestrictionGroupId=" + mcc_restriction_group_id \
              + "&merchantRestrictionGroupId=" + merchant_restriction_group_id \
              + "&countryRestrictionGroupId=" + country_restriction_group_id \
              + "&pageNumber=" + page_number \
              + "&pageCount=" + page_count \
              + "&sortBy=" + sort_by \
              + "&sortOrder=" + sort_order \
              + "&createdDateFrom=" + created_date_from \
              + "&createdDateTo=" + created_date_to \
              + "&updatedDateFrom=" + updated_date_from \
              + "&updatedDateTo=" + updated_date_to

        payload = {}
        headers = {
            'Accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        # Response
        print(response.text.encode('utf8'))

    def test_GET_cards__id(self):
        print("test_GET_cards__id")

        id = 11

        url = "https://sandbox.treezor.com/v1/index.php/cards/" + str(id)

        payload = {}
        headers = {
            'Accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

    def test_PUT_cards__id(self):
        print("test_PUT_cards__id")

        id = 11
        access_signature = "access_signature"
        mcc_restriction_group_id = "mcc_restriction_group_id"
        merchant_restriction_group_id = "merchant_restriction_group_id"
        country_restriction_group_id = "country_restriction_group_id"
        access_tag = "access_tag"
        access_user_id = "access_user_id"
        access_user_ip = "access_user_ip"

        url = "https://sandbox.treezor.com/v1/index.php/cards/" + str(id) \
              + "?accessSignature=" + access_signature \
              + "&mccRestrictionGroupId=" + mcc_restriction_group_id \
              + "&merchantRestrictionGroupId=" + merchant_restriction_group_id \
              + "&countryRestrictionGroupId=" + country_restriction_group_id \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip

        payload = {}
        headers = {
            'Accept': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

    def test_POST_cards_CreateVirtual(self):
        print("test_POST_cards_CreateVirtual")

        access_signature = "access_signature"
        user_id = "user_id"
        wallet_id = "wallet_id"
        perms_group = "perms_group"
        card_tag = "card_tag"
        batch_delivery_id = "batch_delivery_id"
        limit_atm_year = "limit_atm_year"
        limit_atm_month = "limit_atm_month"
        limit_atm_week = "limit_atm_week"
        limit_atm_day = "limit_atm_day"
        limit_atm_all = "limit_atm_all"
        limit_payment_year = "limit_payment_year"
        limit_payment_month = "limit_payment_month"
        limit_payment_week = "limit_payment_week"
        limit_payment_day = "limit_payment_day"
        limit_payment_all = "limit_payment_all"
        payment_daily_limit = "payment_daily_limit"
        pin = "pin"
        card_print = "card_print"
        anonymous = "anonymous"
        send_to_parent = "send_to_parent"
        mcc_restriction_group_id = "mcc_restriction_group_id"
        merchant_restriction_group_id = "merchant_restriction_group_id"
        country_restriction_group_id = "country_restriction_group_id"
        access_tag = "access_tag"
        access_user_id = "access_user_id"
        access_user_ip = "access_user_ip"

        url = "https://sandbox.treezor.com/v1/index.php/cards/CreateVirtual?" \
              + "accessSignature=" + access_signature \
              + "&userId=" + user_id \
              + "&walletId=" + wallet_id \
              + "&permsGroup=" + perms_group \
              + "&cardTag=" + card_tag \
              + "&batchDeliveryId=" + batch_delivery_id \
              + "&limitAtmYear=" + limit_atm_year \
              + "&limitAtmMonth=" + limit_atm_month \
              + "&limitAtmWeek=" + limit_atm_week \
              + "&limitAtmDay=" + limit_atm_day \
              + "&limitAtmAll=" + limit_atm_all \
              + "&limitPaymentYear=" + limit_payment_year \
              + "&limitPaymentMonth=" + limit_payment_month \
              + "&limitPaymentWeek=" + limit_payment_week \
              + "&limitPaymentDay=" + limit_payment_day \
              + "&limitPaymentAll=" + limit_payment_all \
              + "&paymentDailyLimit=" + payment_daily_limit \
              + "&pin=" + pin \
              + "&cardPrint=" + card_print \
              + "&anonymous=" + anonymous \
              + "&sendToParent=" + send_to_parent \
              + "&mccRestrictionGroupId=" + mcc_restriction_group_id \
              + "&merchantRestrictionGroupId=" + merchant_restriction_group_id \
              + "&countryRestrictionGroupId=" + country_restriction_group_id \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip

        payload = {}
        headers = {
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

    def test_POST_cards_RequestPhysical(self):
        print("test_POST_cards_RequestPhysical")

        access_signature = "access_signature"
        user_id = "user_id"
        wallet_id = "wallet_id"
        perms_group = "perms_group"
        card_tag = "card_tag"
        batch_delivery_id = ""
        limit_atm_year = "limit_atm_year"
        limit_atm_month = "limit_atm_month"
        limit_atm_week = "limit_atm_week"
        limit_atm_day = "limit_atm_day"
        limit_atm_all = "limit_atm_all"
        limit_payment_year = "limit_payment_year"
        limit_payment_month = "limit_payment_month"
        limit_payment_week = "limit_payment_week"
        limit_payment_day = "limit_payment_day"
        limit_payment_all = "limit_payment_all"
        payment_daily_limit = "payment_daily_limit"
        pin = "pin"
        card_print = "card_print"
        anonymous = "anonymous"
        send_to_parent = "send_to_parent"
        mcc_restriction_group_id = "mcc_restriction_group_id"
        merchant_restriction_group_id = "merchant_restriction_group_id"
        country_restriction_group_id = "country_restriction_group_id"
        access_tag = "access_tag"
        access_user_id = "access_user_id"
        access_user_ip = "accessUserIp"

        url = "https://sandbox.treezor.com/v1/index.php/cards/RequestPhysical?" \
              + "accessSignature=" + access_signature \
              + "&userId=" + user_id \
              + "&walletId=" + wallet_id \
              + "&permsGroup=" + perms_group \
              + "&cardTag=" + card_tag \
              + "&batchDeliveryId=" + batch_delivery_id \
              + "&limitAtmYear=" + limit_atm_year \
              + "&limitAtmMonth=" + limit_atm_month \
              + "&limitAtmWeek=" + limit_atm_week \
              + "&limitAtmDay=" + limit_atm_day \
              + "&limitAtmAll=" + limit_atm_all \
              + "&limitPaymentYear=" + limit_payment_year \
              + "&limitPaymentMonth=" + limit_payment_month \
              + "&limitPaymentWeek=" + limit_payment_week \
              + "&limitPaymentDay=" + limit_payment_day \
              + "&limitPaymentAll=" + limit_payment_all \
              + "&paymentDailyLimit=" + payment_daily_limit \
              + "&pin=" + pin \
              + "&cardPrint=" + card_print \
              + "&anonymous=" + anonymous \
              + "&sendToParent=" + send_to_parent \
              + "&mccRestrictionGroupId=" + mcc_restriction_group_id \
              + "&merchantRestrictionGroupId=" + merchant_restriction_group_id \
              + "&countryRestrictionGroupId=" + country_restriction_group_id \
              + "&accessTag=" + access_tag \
              + "&accessUserId=" + access_user_id \
              + "&accessUserIp=" + access_user_ip

        payload = {}
        headers = {
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

    def test_POST_cards_Register3DS(self):
        print("test_POST_cards_Register3DS")

    def test_GET_cardimages(self):
        print("test_GET_cardimages")

    def test_PUT_cards__id__activate(self):
        print("test_PUT_cards__id__activate")

    def test_PUT_cards__id__changepin(self):
        print("test_PUT_cards__id__changepin")

    def test_PUT_cards__id__convertvirtual(self):
        print("test_PUT_cards__id__convertvirtual")

    def test_PUT_cards__id__Limits(self):
        print("test_PUT_cards__id__Limits")

    def test_PUT_cards__id__LockUnlock(self):
        print("")

    def test_PUT_cards__id__Options(self):
        print("test_PUT_cards__id__Options")

    def test_PUT_cards__id__Regenerate(self):
        print("test_PUT_cards__id__Regenerate")

    def test_PUT_cards__id_setpin(self):
        print("test_PUT_cards__id_setpin")

    def test_PUT_cards__id__UnblockPIN(self):
        print("test_PUT_cards__id__UnblockPIN")


class cardDigitalizations(unittest.TestCase):
    def test_GET_cardDigitalizations(self):
        print("test_GET_cardDigitalizations")

    def test_DELETE_cardDigitalizations__id(self):
        print("test_DELETE_cardDigitalizations__id")

    def test_GET_cardDigitalizations__id(self):
        print("test_GET_cardDigitalizations__id")

    def test_PUT_cardDigitalizations__id(self):
        print("test_PUT_cardDigitalizations__id")


class cardReserve(unittest.TestCase):
    def test_GET_cardReserves__id(self):
        print("test_GET_cardReserves__id")

    def test_POST_cardReserves_AddTo(self):
        print("test_POST_cardReserves_AddTo")

    def test_POST_cardReserves_Check(self):
        print("test_POST_cardReserves_Check")


class cardtransaction(unittest.TestCase):
    def test_GET_cardtransactions(self):
        print("test_GET_cardtransactions")

    def test_GET_cardtransactions__id(self):
        print("test_GET_cardtransactions__id")


class countryRestrictionGroups(unittest.TestCase):
    def test_GET_countryRestrictionGroups(self):
        print("test_GET_countryRestrictionGroups")

    def test_POST_countryRestrictionGroups(self):
        print("test_POST_countryRestrictionGroups")

    def test_delete_countryRestrictionGroups__id(self):
        print("test_delete_countryRestrictionGroups__id")

    def test_get_countryRestrictionGroups__id(self):
        print("test_get_countryRestrictionGroups__id")

    def test_put_countryRestrictionGroups__id(self):
        print("test_put_countryRestrictionGroups__id")


class document(unittest.TestCase):
    def test_get_documents(self):
        print("test_get_documents")

    def test_post_documents(self):
        print("test_post_documents")

    def test_delete_documents__id(self):
        print("test_delete_documents__id")

    def test_get_documents__id(self):
        print("test_get_documents__id")

    def test_put_documents__id(self):
        print("test_put_documents__id")


class heartbeat(unittest.TestCase):
    def test_get_heartbeats(self):
        print("test_get_heartbeats")


class issuerInitiatedDigitizationData(unittest.TestCase):
    def test_get_issuerInitiatedDigitizationDatas(self):
        print("test_get_issuerInitiatedDigitizationDatas")

    def test_post_issuerInitiatedDigitizationDatas(self):
        print("test_post_issuerInitiatedDigitizationDatas")


class mandate(unittest.TestCase):
    def test_get_mandates(self):
        print("test_get_mandates")

    def test_post_mandates(self):
        print("test_post_mandates")

    def test_delete_mandates__id(self):
        print("test_delete_mandates__id")

    def test_get_mandates__id(self):
        print("test_get_mandates__id")

    def test_put_mandates__id__Sign(self):
        print("test_put_mandates__id__Sign")

    def test_put_mandates__id__ResendOtp(self):
        print("test_put_mandates__id__ResendOtp")


class mccRestrictionGroups(unittest.TestCase):
    def test_get_mccRestrictionGroups(self):
        print("test_get_mccRestrictionGroups")

    def test_post_mccRestrictionGroups(self):
        print("test_post_mccRestrictionGroups")

    def test_delete_mccRestrictionGroups__id(self):
        print("test_delete_mccRestrictionGroups__id")

    def test_get_mccRestrictionGroup__id(self):
        print("test_get_mccRestrictionGroup__id")

    def test_put_mccRestrictionGroups__id(self):
        print("test_put_mccRestrictionGroups__id")


class merchantIdRestrictionGroups(unittest.TestCase):
    def test_get_merchantIdRestrictionGroups(self):
        print("test_get_merchantIdRestrictionGroups")

    def test_post_merchantIdRestrictionGroups(self):
        print("test_post_merchantIdRestrictionGroups")

    def test_delete_merchantIdRestrictionGroups__id(self):
        print("test_delete_merchantIdRestrictionGroups__id")

    def test_get_merchantIdRestrictionGroups__id(self):
        print("test_get_merchantIdRestrictionGroups__id")

    def test_put_merchantIdRestrictionGroups__id(self):
        print("test_put_merchantIdRestrictionGroups__id")

    def test_put_merchantIdRestrictionGroups__id__DeltaUpdate(self):
        print("test_put_merchantIdRestrictionGroups__id__DeltaUpdate")


class payin(unittest.TestCase):
    def test_get_payins(self):
        print("test_get_payins")

    def test_post_payins(self):
        print("test_post_payins")

    def test_delete_payins__id(self):
        print("test_delete_payins__id")

    def test_get_payins__id(self):
        print("test_get_payins__id")


class payinrefund(unittest.TestCase):
    def test_get_payinrefunds(self):
        print("test_get_payinrefunds")

    def test_post_payinrefunds(self):
        print("test_post_payinrefunds")

    def test_delete_payinrefunds__id(self):
        print("test_delete_payinrefunds__id")

    def test_get_payinrefunds__id(self):
        print("test_get_payinrefunds__id")


class payout(unittest.TestCase):
    def test_get_payouts(self):
        print("test_get_payouts")

    def test_post_payouts(self):
        print("test_post_payouts")

    def test_delete_payouts__id(self):
        print("test_delete_payouts__id")

    def test_get_payouts__id(self):
        print("test_get_payouts__id")


class payoutRefunds(unittest.TestCase):
    def test_get_payoutRefunds(self):
        print("test_get_payoutRefunds")


class taxResidence(unittest.TestCase):
    def test_get_taxResidences(self):
        print("test_get_taxResidences")

    def test_post_taxResidences(self):
        print("test_post_taxResidences")

    def test_delete_taxResidences__id(self):
        print("test_delete_taxResidences__id")

    def test_get_taxResidences__id(self):
        print("test_get_taxResidences__id")

    def test_put_taxResidences__id(self):
        print("test_put_taxResidences__id")


class transaction(unittest.TestCase):
    def test_get_transactions(self):
        print("test_get_transactions")

    def test_get_transactions__id(self):
        print("test_get_transactions__id")


class transfer(unittest.TestCase):
    def test_get_transfers(self):
        print("test_get_transfers")

    def test_post_transfers(self):
        print("test_post_transfers")

    def test_delete_transfers__id(self):
        print("test_delete_transfers__id")

    def test_get_transfers__id(self):
        print("test_get_transfers__id")


class transferrefund(unittest.TestCase):
    def test_get_transferrefunds(self):
        print("test_get_transferrefunds")

    def test_post_transferrefunds(self):
        print("test_post_transferrefunds")

    def test_delete_transferrefunds__id(self):
        print("test_delete_transferrefunds__id")

    def test_get_transferrefunds__id(self):
        print("test_get_transferrefunds__id")


class user(unittest.TestCase):
    def test_get_users(self):
        print("test_get_users")

    def test_post_users(self):
        print("test_post_users")

    def test_delete_users__id(self):
        print("test_delete_users__id")

    def test_get_users__id(self):
        print("test_get_users__id")

    def test_put_users__id(self):
        print("test_put_users__id")

    def test_put_users__id__Kycreview(self):
        print("test_put_users__id__Kycreview")


class virtualibans(unittest.TestCase):
    def test_get_virtualibans(self):
        print("test_get_virtualibans")

    def test_post_virtualibans(self):
        print("test_post_virtualibans")

    def test_get_virtualibans__id(self):
        print("test_get_virtualibans__id")

    def test_put_virtualibans__id(self):
        print("test_put_virtualibans__id")


class wallet(unittest.TestCase):
    def test_get_wallets(self):
        print("test_get_wallets")

    def test_post_wallets(self):
        print("test_post_wallets")

    def test_delete_wallets__id(self):
        print("test_delete_wallets__id")

    def test_get_wallets__id(self):
        print("test_get_wallets__id")

    def test_put_wallets__id(self):
        print("test_put_wallets__id")


if __name__ == '__main__':
    unittest.main()
