from ui_poms.ise.Policy.Policy import Policy
from selenium_core.selenium_ui_elements import *
from selenium_core.selenium_ui_base_page import BasePage
from selenium.webdriver.common.by import By


class PolicySetsAuthenticationAndAutherizaton(BasePage):
    def __init__(self, app, logger):
        super().__init__(app, logger)

    ###  PAGE UI ELEMENTSAND ACTIONS

    @property
    def navigate_policy_sets(self):
        return Hover(By.XPATH, "//a[@href='#policy/policy_grouping']", self.driver)

    def navigate_from_parent(self):
        self.navigate_policy_sets.click()

    def get_parent_page(self):
        return Policy(self.app, self.logger)

    ######   PAGE UI ELEMENTS  #######################

    ####  add button#################3
    @property
    def policy_sets_add_button(self):
        return Button(By.XPATH,
                      "((.//*[@class='dijit dijitToolbar'])[1]//*[@class='dijitReset dijitStretch dijitButtonContents dijitDownArrowButton'])[1] ",
                      self.driver)

    ##### add button dropdown ##############33
    @property
    def policy_sets_add_button_dropdown_selection(self):
        return Button(By.XPATH, " .//*[contains(text(),'Create Above')] ", self.driver)

    ######  clicking first EDIT button  ##################
    @property
    def first_edit_button(self):
        return Button(By.XPATH, " (//a[contains(text(),'Edit')])[1]", self.driver)

    ########  policy name  in first edit button ############
    @property
    def policy_name(self):
        return Input(By.XPATH, " (//input[@class='dijitReset'])[1] ", self.driver)

    #### policy description  in first edit button ################
    @property
    def policy_description(self):
        return Input(By.XPATH, "(//input[@class='dijitReset'])[2]", self.driver)

    ####    conditions dropdown button############
    @property
    def policy_condition_drop_down(self):
        return Button(By.XPATH,
                      ".//*[@class='xwtRepeaterItem repeaterItemOddRow']//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand']",
                      self.driver)

    ###### conditions dropdown selection(selecting previous library)  #############
    @property
    def drop_down_selection(self):
        return Button(By.XPATH,
                      "(.//*[@class='cpm_init_button_view'])[1]//*[contains(text(),'Select Existing Condition from Library')]",
                      self.driver)

    ####  selecting condition name drop down button #############
    @property
    def condition_name_dropdown1(self):
        return Button(By.XPATH,
                      " (.//*[@class='xwtRepeaterItem']//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ",
                      self.driver)

    ### selecting compoundcondition########################
    @property
    def compound_condition(self):
        return Button(By.XPATH, " //div[contains(text(),'Compound Condition')]", self.driver)

    ### selecting one condition from compound condition  #################

    @property
    def compound_condition_selection(self):
        return Button(By.XPATH, "//div[contains(text(),'Wireless_802.1X')]", self.driver)

    ### selecting first DONE button #################
    @property
    def done_button(self):
        return Button(By.XPATH, "(//*[contains(text(),'Done')])[1] ", self.driver)

    ####################### first   authentication policy ##############################################



    ##  AUTHENTICATION POLICY EDIT BUTTON DROP DOWN  ###########

    @property
    def first_authentication_edit_button_dropdown(self):
        return Button(By.XPATH, " (//span[@class='repeaterDataItemActionsDropDown'])[1] ", self.driver)

        ###SELECTING NEW row above ###############

    @property
    def first_selcting_insert_new_row_above(self):
        return Button(By.XPATH, " (//td[contains(text(),'Insert new row above')])[1]", self.driver)

        ##### Authentication Policy Name############################

    @property
    def first_authentication_standard_rule1(self):
        return Input(By.XPATH, "(//input[@class='dijitReset'])[1] ", self.driver)

        ####### AUTHENTICATION POLICY CONDITIONS ###############

    @property
    def first_authentication_rule1_conditions_dropdown(self):
        return Button(By.XPATH,
                      " (//span[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[1]",
                      self.driver)

        ######### clicking pn ''selecting existing library''############

    @property
    def first_authentication_selecting_existing_condition_from_library(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Select Existing Condition from Library')])[1] ",
                      self.driver)
        ########## condition names drop down#########################################

    @property
    def first_authentication_condition_name_dropdown(self):
        return Button(By.XPATH,
                      "(//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[3] ",
                      self.driver)

    ##########selecting the compound condition########################################

    @property
    def first_authentication_selecting_compound_condition(self):
        return Button(By.XPATH, "//*[contains(text(),'Compound Condition')]", self.driver)


        #############selecting the condition name##########################################

    @property
    def first_authentication_selecting_condition_name(self):
        return Button(By.XPATH, "//*[contains(text(),'Switch_Local_Web_Authentication')]", self.driver)
        #######PROTOCOL DROP DOWN #######################################

    @property
    def first_authentication_protocol_drop_down(self):
        return Button(By.XPATH,
                      " (.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1] ",
                      self.driver)

        ######################selecting allowed protocol  drop down  ########################################

    @property
    def first_authentication_allowed_protocol_drop_down(self):
        return Button(By.XPATH, " //*[contains(text(),'Allowed Protocols')]", self.driver)

        #################### selecting the protocol###########################

    @property
    def first_authentication_selecting_default_network_access_protocol(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Default Network Access')])[3] ", self.driver)

        #################police use #########################################

    @property
    def first_authentication_use_button_drop_down(self):
        return Button(By.XPATH,
                      " (.//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[3] ",
                      self.driver)

        #################selecting the identity resourse drop down #####################################

    @property
    def first_authentication_identity_resourse_drop_down(self):
        return Button(By.XPATH,
                      " (//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2]",
                      self.driver)

        #########selecting the identity resourse ##########################################

    @property
    def first_authentication_selecting_identity_resourse(self):
        return Button(By.XPATH, " //div[contains(text(),'Internal Endpoints')] ", self.driver)

        ###DONE buton###############################

    @property
    def first_authentication_done_button(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Done')])[1] ", self.driver)

    #################second authenticaion policy #######################################################


    ########SECOND AUTHONTICATION pOLICY  ##################
    #######################################################

    #######edit drop down to create second authontication policy ##############################
    @property
    def authentication_secnd_edit_drop_down(self):
        return Button(By.XPATH,
                      "(//a[contains(text(),'Edit')])[3]/../span[@class='repeaterDataItemActionsDropDown'] ",
                      self.driver)
        ########selecting new role above option from edit drop down ################

    @property
    def authentication_secnd_selecting_new_row_above(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Insert new row above')])[1] ", self.driver)
        ###########selecting rule name  #####################################################

    @property
    def authentication_secnd_rule(self):
        return Input(By.XPATH, " (.//input[@class='dijitReset'])[1] ", self.driver)

        ###############conditions drop down button##############################3333

    @property
    def authentication_secnd_condition_dropdown_button(self):
        return Button(By.XPATH,
                      "(//span[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[1] ",
                      self.driver)

        #############selecting existing condition from library ##########################################

    @property
    def authentication_secnd_seclecting_existing_condition(self):
        return Button(By.XPATH, " (//*[contains(text(),'Select Existing Condition from Library')])[1] ",
                      self.driver)

        ############# condition name drop downbutton#########################3

    @property
    def authentication_secnd_selecting_condition_name_drop_down_button(self):
        return Button(By.XPATH,
                      " (.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[3]",
                      self.driver)

        ############## selecting compound condition #####################

    @property
    def authentication_secnd_selecting_compound_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Compound Condition')]", self.driver)

        ############selecting a condition form compound condition###############################

    @property
    def authentication_secnd_selecting_condition1(self):
        return Button(By.XPATH, "//*[contains(text(),'WLC_Web_Authentication')] ", self.driver)

        ###############selecting settings drop down button in conditions###########################

    @property
    def authentication_secnd_selecting_settings_drop_down_button(self):
        return Button(By.XPATH,
                      "(.//button[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ",
                      self.driver)

        ##########selecting ADD condition from library buttom ###################

    @property
    def authentication_secnd_selecting_add_condition_from_library_button(self):
        return Button(By.XPATH, "(//td[contains(text(),'Add Condition from Library')])[2]", self.driver)

        ################selecting and operater drop down button################################################

    @property
    def authentication_secnd_selecting_AND_operater_drop_down(self):
        return Button(By.XPATH, "(//div[@class='dijitArrowButtonInner'])[2] ", self.driver)

        ###################selecting  AND operater###############################

    @property
    def authentication_secnd_selecting_And_operater(self):
        return Button(By.XPATH, " (//div[contains(text(),'AND')]) ", self.driver)

        ##########selecting another condition from compound condition drop down####################################

    @property
    def authentication_secnd_selecting_condition2_drop_down_button(self):
        return Button(By.XPATH,
                      " (.//button[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[7] ",
                      self.driver)

        ##################selecting compound condition#########################

    @property
    def authenticaion_secnd_selecting_compound_condition(self):
        return Button(By.XPATH, "(.//div[contains(text(),'Compound Condition')])[1]", self.driver)

        ##############selecting the condition name###############################################################

    @property
    def authentication_secnd_selecting_condition2(self):
        return Button(By.XPATH, " (.//div[contains(text(),'Switch_Web_Authentication')]) ", self.driver)

        ####################selecting allow protocols drop down button################################3

    @property
    def authentication_secnd_selecting_allow_protocols_drop_down(self):
        return Button(By.XPATH,
                      "(//button[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1] ",
                      self.driver)

        ######################selcting allow protocols ######################################################

    @property
    def authentication_secnd_selecting_allow_protocols(self):
        return Button(By.XPATH, "//div[contains(text(),'Allowed Protocols')] ", self.driver)

        #####################select network default access Button###############################333

    @property
    def authentication_secnd_selecting_default_network_access(self):
        return Button(By.XPATH, " //div[contains(text(),'Default Network Access')] ", self.driver)

        #######################internal users drop down button#################################333333

    @property
    def authentication_secnd_selecting_inernal_users_drop_down(self):
        return Button(By.XPATH,
                      " (.//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[3]",
                      self.driver)

        #####################selecting identity source drop down ######################################

    @property
    def authentication_secnd_selecting_identity_sourse_drop_down(self):
        return Button(By.XPATH,
                      "(.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2]",
                      self.driver)

        ######################selecting one from identity sourse list  ###################################

    @property
    def authentication_secnd_selecting_identity_sourse_list(self):
        return Button(By.XPATH, " .//*[contains(text(),'All_AD_Join_Points')]", self.driver)

        ######################selecting DONE button###########################################################3

    @property
    def authentication_secnd_selecting_done_button(self):
        return Button(By.XPATH, " (.//a[contains(text(),'Done')])[1] ", self.driver)

    ##################################################################################################################
    ##################third authentication policy elements ############################################################



    @property
    def third_authentication_edit_drop_down_button(self):
        return Button(By.XPATH, " (//*[contains(text(),'Edit')])[4]/../*[@class='repeaterDataItemActionsDropDown'] ",
                      self.driver)


        ################selecting new row above #################################################

    @property
    def third_authentication_selecting_insert_new_row_above(self):
        return Button(By.XPATH, "(//td[contains(text(),'Insert new row above')])[1]", self.driver)

        ##############giving authentication rule 3#################################################################

    @property
    def third_authentication_policy_rule_3(self):
        return Input(By.XPATH, "(//div/div/input[@class='dijitReset'])[1]", self.driver)

        ####################### clicking on condiions drop down button ##############################################

    @property
    def third_authentication_policy_conditions_dropdown(self):
        return Button(By.XPATH,
                      "(//span/span/span[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[1]",
                      self.driver)

        #######################selecting existing condition from the library #################################

    @property
    def third_authentication_selecting_existing_condition_from_library(self):
        return Button(By.XPATH, "(//*[contains(text(),'Select Existing Condition from Library')])[1]", self.driver)

        ######################selecting condition name drop down button ##################################

    @property
    def third_authentication_selecting_condotion_name(self):
        return Button(By.XPATH,
                      "(.//button[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[3]",
                      self.driver)

        #######################selecting the compound condition ####################################3

    @property
    def third_authentication_selecting_compound_condition(self):
        return Button(By.XPATH, "//*[contains(text(),'Compound Condition')]", self.driver)

    ########################### selecting wireless_MAB  conditions #######################################
    @property
    def third_authentication_selecting_wireless_mab_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Wireless_MAB')]", self.driver)

    ###############################selecting the allow protocolsdrop down button ######################
    @property
    def third_authentication_selecting_allow_protocols_drop_down_button(self):
        return Button(By.XPATH,
                      "(//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1]",
                      self.driver)

    ##################################selcting  allowed protocols #######################################
    @property
    def third_authentication_selecting_allowed_protocols(self):
        return Button(By.XPATH, " //*[contains(text(),'Allowed Protocols')]", self.driver)

    ############################selecting  default network access ##################################
    @property
    def third_authentication_selecting_default_network_access(self):
        return Button(By.XPATH, "(//*[contains(text(),'Default Network Access')])[3]", self.driver)

    ###############################selcting internel users drop down ########################################
    @property
    def third_authentication_selectig_inernal_users_drop_down_button(self):
        return Button(By.XPATH,
                      " (//*[contains(text(),'use')]//..//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[3]",
                      self.driver)

    ###################selecting he identity scource drop down ##############################
    @property
    def third_authentication_selecting_identity_source_drop_down_button(self):
        return Button(By.XPATH,
                      "(//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ",
                      self.driver)

    ################################selecting a identity resourse from identity resourse list #######################
    @property
    def third_authentication_selecting_portal_sequence_resourse_from_identity_resourse(self):
        return Button(By.XPATH, " //*[contains(text(),'MyDevices_Portal_Sequence')]", self.driver)


        ##############################selecting done  button ###################################

    @property
    def third_authentication_selecting_done_button(self):
        return Button(By.XPATH, "(//a[contains(text(),'Done')])[1]", self.driver)

###################minimizing the authentication drop down ###################################################################3
    @property
    def minimizing_authentication_drop_down(self):
        return Button(By.XPATH," .//*[@id='authnPolicyGroupTitlePane_arrowNodeInner']", self.driver)







#######################################################################################################################################
#####################################################################################################################################

#####################       AUTHORIZATION POLICY   ######################################################
#####################################################################################################################
    ########## edit drop down for first authorization policy################################

    @property
    def selecting_first_authorization_policy_edit_button_dropdown(self):
        return Button(By.XPATH, " .//*[@id='authZContainer']//*[@class='repeaterDataItemActionsDropDown']",
                      self.driver)

    ###################### selecting insert new row above ########################################
    @property
    def selecing_first_authorization_insert_new_row_above(self):
        return Button(By.XPATH, "//*[contains(text(),'Insert New Rule Above')]", self.driver)

    #######################authorization policy rule 1#########################################
    @property
    def selecting_first_authorization_policy_rule(self):
        return Input(By.XPATH, " (.//*[@id='authZContainer']//..//div/input[@class='dijitReset'])[4]", self.driver)

    ######################### clicking on any groups drop down ########################
    @property
    def first_authorization_groups_drop_down_button(self):
        return Button(By.XPATH,
                      " (.//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[7]",
                      self.driver)

    ################### clicking any drop down button################################33
    @property
    def first_authorization_any_drop_down_button(self):
        return Button(By.XPATH,
                      "(.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1]",
                      self.driver)

    #########################selecting user identity groups ##########################################
    @property
    def first_authorization_user_identity_groups(self):
        return Button(By.XPATH, "(//*[contains(text(),'User Identity Groups')])[2] ", self.driver)

    #################### selecting one user identity group ########################################
    @property
    def first_authorization_chaitu_user_identity_group(self):
        return Button(By.XPATH, "//*[contains(text(),'(CHAITU) Guest Access Group')] ", self.driver)

    ######closig group drop down ############################################
    @property
    def first_authorization_groups_drop_down_button_close(self):
        return Button(By.XPATH,
                      " (.//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[7]",
                      self.driver)

    #############################selecting the conditions drop down button#############################
    @property
    def first_authorization_conditions_drop_down_button(self):
        return Button(By.XPATH,
                      "(.//*[@id='authZContainer']//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[8] ",
                      self.driver)

    """
    #############################selecting the existing condiiition from library ########################
    @property
    def first_authorization_existing_condition_from_library(self):
        return Button(By.XPATH, "(.//*[contains(text(),'Select Existing Condition from Library')])[1] ", self.driver)

    ####################selecting condition name drop down#########################################
    @property
    def first_authorization_condition_name_drop_down(self):
        return Button(By.XPATH, "(.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ", self.driver)

    ########################### selectingthe compound condition ####################################
    @property
    def first_authorization_compound_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Compound Conditions')]", self.driver)

    ###########################guest flow condition#####################################################
    @property
    def first_authorization_Guest_flow_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Guest_Flow')]", self.driver)
    """

    ################condition drop down close ######################################################################

    @property
    def first_authorization_conditions_drop_down_button_close(self):
        return Button(By.XPATH,
                      "(.//*[@id='authZContainer']//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[8] ",
                      self.driver)

    ########### permissions drop down######################################################
    @property
    def first_authorization_permissions_drop_down_buton(self):
        return Button(By.XPATH,
                      "(.//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[9] ",
                      self.driver)

        #####################################################################################################################################################
        #####################################################################################################################
        #############################selecting the existing condiiition from library ########################

    @property
    def first_authorization_existing_condition_from_library(self):
        return Button(By.XPATH, "(.//*[contains(text(),'Select Existing Condition from Library')])[1] ",
                      self.driver)

    ####################selecting condition name drop down#########################################
    @property
    def first_authorization_condition_name_drop_down(self):
        return Button(By.XPATH,
                      "(.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ",
                      self.driver)

    ########################### selectingthe compound condition ####################################
    @property
    def first_authorization_compound_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Compound Conditions')]", self.driver)

    ###########################guest flow condition#####################################################
    @property
    def first_authorization_Guest_flow_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Guest_Flow')]", self.driver)

    @property
    def first_authorization_conditions_drop_down_button_close(self):
        return Button(By.XPATH,
                      "(.//*[@id='authZContainer']//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[8] ",
                      self.driver)

    @property
    def first_authorization_permissions_drop_down_buton(self):
        return Button(By.XPATH,
                      "(.//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[9] ",
                      self.driver)

    #####################################################################################################################
    #######################################################################################################################
    ########################select an item drop down######################################
    @property
    def first_authorization_item_drop_down(self):
        return Button(By.XPATH,
                      " (.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1]",
                      self.driver)

    ########################## security group##################################################
    @property
    def first_authorization_security_group(self):
        return Button(By.XPATH, " //div[contains(text(),'Security Group')]", self.driver)

    ################################selecting chaitureddy securiy group##############################
    @property
    def first_authorization_chaitureddy_security_group(self):
        return Button(By.XPATH, "//*[contains(text(),'ChaituReddy')] ", self.driver)

    ############################### selecting Done button #########################
    @property
    def first_authorization_policy_done_button(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Done')])[3]", self.driver)





        ##########################################################################################################################################
        ################   second autherzation policy   #######################################################
        ###########################################################################################################################################


        ##########  edit button ###########################################

    @property
    def selecting_second_authorization_policy_edit_button_dropdown(self):
        return Button(By.XPATH, " (.//*[@id='authZContainer']//*[@class='repeaterDataItemActionsDropDown'])[2]",
                      self.driver)

    ###################### selecting insert new row above ########################################
    @property
    def selecing_second_authorization_insert_new_row_above(self):
        return Button(By.XPATH, "//*[contains(text(),'Insert New Rule Above')]", self.driver)

    #######################authorization policy rule 1#########################################
    @property
    def selecting_second_authorization_policy_rule2(self):
        return Input(By.XPATH, " (.//*[@id='authZContainer']//..//div/input[@class='dijitReset'])[4]", self.driver)

    ######################### clicking on any groups drop down ########################
    @property
    def second_authorization_groups_drop_down_button(self):
        return Button(By.XPATH,
                      " (.//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[7]",
                      self.driver)

    ################### clicking any drop down button################################33
    @property
    def second_authorization_any_drop_down_button(self):
        return Button(By.XPATH,
                      "(.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1]",
                      self.driver)

    #########################selecting user identity groups ##########################################
    @property
    def second_authorization_user_identity_groups(self):
        return Button(By.XPATH, "(//*[contains(text(),'User Identity Groups')])[2] ", self.driver)

    #################### selecting one user identity group ########################################
    @property
    def second_authorization_base_onboard_posture_group(self):
        return Button(By.XPATH, "//*[contains(text(),'Baseline-onboard-posture')] ", self.driver)


        ###############selecting plus button for adding second group ############################

    @property
    def second_authorization_plus_button_for_second_group(self):
        return Button(By.XPATH, " (//*[@class='dijitReset dijitStretch xwt-IconButtonContents'])[2]", self.driver)

        ########################group name drop down ##################################################

    @property
    def second_authorization_second_drop_down_for_group(self):
        return Button(By.XPATH,
                      "  //*[@ class='xwtRepeaterItem repeaterItemEvenRow']//*[@ class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton']",
                      self.driver)


        ###########################selecting the end point identity  groups #######################################################

    @property
    def second_authorization_end_point_identity_group(self):
        return Button(By.XPATH, "(//*[contains(text(),'Endpoint Identity Groups')])[1] ", self.driver)


        ####################selecting registred group ###############################

    @property
    def second_authorization_registerd_devices(self):
        return Button(By.XPATH, "(//*[contains(text(),'RegisteredDevices')]) ", self.driver)


        #####################closing the group drop down button #########################################################

    @property
    def second_authorization_groups_drop_down_close_button(self):
        return Button(By.XPATH,
                      " (.//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[7]",
                      self.driver)

        ##################selecting the codition drop down button#######################################

    @property
    def second_authorization_condition_drop_down(self):
        return Button(By.XPATH, " (//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[8]",
                      self.driver)

    """
###################selecting existing condition from library ############################################################
    @property
    def second_authorization_existing_condition_from_library(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Select Existing Condition from Library')])[1] ",
                      self.driver)

####################### selectingthe condition name drop down #######################################################

    @property
    def second_authorization_condition_name_drop_down(self):
        return Button(By.XPATH, "(.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ", self.driver)


    ########################### selectingthe compound condition ####################################
    @property
    def second_authorization_compound_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Compound Conditions')]", self.driver)

    ###########################EAP -TLS condition#####################################################
    @property
    def second_authorization_EAP_TLS_condition(self):
        return Button(By.XPATH, "  //*[contains(text(),'EAP-TLS')]", self.driver)

    ######################### setting button for adding anoher condition ##########################################

    @property
    def second_authorization_setting_button_for_adding_second_condition(self):
        return Button(By.XPATH, "(//*[@class='xwtRepeaterItem']//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1] ", self.driver)

###########################selecting add condition from library #############################################################
    @property
    def second_authorization_add_condition_from_library(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Add Condition from Library')])[1]", self.driver)



########################selecting condition name drop down #######################################################
    @property
    def second_authorization_condition_2_name_drop_down(self):
        return Button(By.XPATH,"((//*[@class='xwtRepeaterItem'])[2]//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ", self.driver)

############################## selecting the simple condition ###############################################################

    @property
    def second_authorization_condition_2_simple_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Simple Conditions')]", self.driver)

#####################selecting CertRenewalRequired condition ########################

    @property
    def second_authorization_condition_2_CertRenewalRequired(self):
        return Button(By.XPATH, "//*[contains(text(),'CertRenewalRequired')] ", self.driver)

#################selecting the settings drop down button for Adding 3rd condition #######################################

    @property
    def second_authorization_settings_buttons_for_adding_third_condition(self):
        return Button(By.XPATH, " ((//*[@class='xwtRepeaterItem'])[2]//*[@ class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1]", self.driver)

    ###########################selecting add condition from library #############################################################
    @property
    def second_authorization_conditon_3_add_condition_from_library(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Add Condition from Library')])[1]", self.driver)

    ########################selecting condition name drop down #######################################################
    @property
    def second_authorization_condition_3_name_drop_down(self):
        return Button(By.XPATH,
                      "((//*[@class='xwtRepeaterItem'])//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[10] ",
                      self.driver)

    ############################## selecting the compound condition ###############################################################

    @property
    def second_authorization_condition_3_compound_condition(self):
        return Button(By.XPATH, " (//*[contains(text(),'Compound Conditions')])[1]", self.driver)

    #####################selecting EAP _ MSCHAP2  group ########################

    @property
    def second_authorization_condition_3_EAP_MSCHAP(self):
        return Button(By.XPATH, "(//*[contains(text(),'EAP-MSCHAPv2')])[1] ", self.driver)

    ###################################permissions drop down button#######################################3
    @property
    def second_authorization_permision_drop_down_button(self):
        return Button(By.XPATH, " (//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[9]", self.driver)
"""

    #######################################################################################################################################
    #####################################################################################################################################
    #####################################################################################################################
    #####################################################################################################################
    ###################selecting existing condition from library ############################################################
    ##################selecting the codition drop down button#######################################
    @property
    def second_authorization_condition_drop_down(self):
        return Button(By.XPATH, " (//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[8]",
                      self.driver)

    @property
    def second_authorization_existing_condition_from_library(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Select Existing Condition from Library')])[1] ",
                      self.driver)

        ####################### selectingthe condition name drop down #######################################################

    @property
    def second_authorization_condition_name_drop_down(self):
        return Button(By.XPATH,
                      "(.//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ",
                      self.driver)

    ########################### selectingthe compound condition ####################################
    @property
    def second_authorization_compound_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Compound Conditions')]", self.driver)

    ###########################EAP -TLS condition#####################################################
    @property
    def second_authorization_EAP_TLS_condition(self):
        return Button(By.XPATH, "  //*[contains(text(),'EAP-TLS')]", self.driver)

    ######################### setting button for adding anoher condition ##########################################

    @property
    def second_authorization_setting_button_for_adding_second_condition(self):
        return Button(By.XPATH,
                      "(//*[@class='xwtRepeaterItem']//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1] ",
                      self.driver)

        ###########################selecting add condition from library #############################################################

    @property
    def second_authorization_add_condition_from_library(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Add Condition from Library')])[1]", self.driver)



        ########################selecting condition name drop down #######################################################

    @property
    def second_authorization_condition_2_name_drop_down(self):
        return Button(By.XPATH,
                      "((//*[@class='xwtRepeaterItem'])[2]//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ",
                      self.driver)

        ############################## selecting the simple condition ###############################################################

    @property
    def second_authorization_condition_2_simple_condition(self):
        return Button(By.XPATH, " //*[contains(text(),'Simple Conditions')]", self.driver)

        #####################selecting CertRenewalRequired condition ########################

    @property
    def second_authorization_condition_2_CertRenewalRequired(self):
        return Button(By.XPATH, "//*[contains(text(),'CertRenewalRequired')] ", self.driver)

        #################selecting the settings drop down button for Adding 3rd condition #######################################

    @property
    def second_authorization_settings_buttons_for_adding_third_condition(self):
        return Button(By.XPATH,
                      " ((//*[@class='xwtRepeaterItem'])[2]//*[@ class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1]",
                      self.driver)

    ###########################selecting add condition from library #############################################################
    @property
    def second_authorization_conditon_3_add_condition_from_library(self):
        return Button(By.XPATH, " (.//*[contains(text(),'Add Condition from Library')])[1]", self.driver)

    ########################selecting condition name drop down #######################################################
    @property
    def second_authorization_condition_3_name_drop_down(self):
        return Button(By.XPATH,
                      "((//*[@class='xwtRepeaterItem'])//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[10] ",
                      self.driver)

    ############################## selecting the compound condition ###############################################################

    @property
    def second_authorization_condition_3_compound_condition(self):
        return Button(By.XPATH, " (//*[contains(text(),'Compound Conditions')])[1]", self.driver)

    #####################selecting EAP _ MSCHAP2  group ########################

    @property
    def second_authorization_condition_3_EAP_MSCHAP(self):
        return Button(By.XPATH, "(//*[contains(text(),'EAP-MSCHAPv2')])[1] ", self.driver)

    ####################closing the condition drop down ###################################################################

    @property
    def second_authorization_condition_drop_down(self):
        return Button(By.XPATH,
                      " (//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[8] ",
                      self.driver)

    ###################################permissions drop down button#######################################3
    @property
    def second_authorization_permision_drop_down_button(self):
        return Button(By.XPATH, " (//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[9]",
                      self.driver)

    #####################################################################################################################
    ######################################################################################################################################



    ###################################    permissions drop down button             #######################################



    @property
    def second_authorization_permission_selecting_item_drop_down(self):
        return Button(By.XPATH,
                      " ((//*[@class='widgetContainer'])//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[1] ",
                      self.driver)

    #####################selecting the security group ####################################
    @property
    def second_authorization_permission_selecting_security_group(self):
        return Button(By.XPATH, " (//*[contains(text(),'Security Group')])[2] ", self.driver)

    ###############################selecting the network services permissionns ########################
    @property
    def second_authorization_permission_selecting_network_access_permission(self):
        return Button(By.XPATH, " (//*[contains(text(),'Network_Services')]) ", self.driver)

    ##############selecting plus button for adding the second permission #################################
    @property
    def second_authorization_permission_selecting_plus_buuton_for_ading_second_permission(self):
        return Button(By.XPATH,
                      " ((//*[@class='widgetContainer'])//button[@class='dijitReset dijitStretch xwt-IconButtonContents'])[2] ",
                      self.driver)

    #####################selecting a item drop down second time ######################################
    @property
    def second_authorization_permission_selecting_item_drop_down_second_time(self):
        return Button(By.XPATH,
                      " (//*[@class='widgetContainer']//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[2] ",
                      self.driver)

    ###############selecting standard profile #########################################################
    @property
    def second_authorization_permission_selecting_standard_profile(self):
        return Button(By.XPATH, " (//*[@class='xwtObjectSelectorListTextDisabled xwtObjectSelectorListText'])[2]",
                      self.driver)

    ############################### selecting permit access ###########################################################
    @property
    def second_authorization_permission_selecting_permit_access(self):
        return Button(By.XPATH, " //*[contains(text(),'PermitAccess')] ", self.driver)

    #######################selecting the plus button for third permission  #############################
    @property
    def second_authorization_permission_selecting_plus_buuton_for_ading_third_permission(self):
        return Button(By.XPATH,
                      " (//*[@class='widgetContainer']//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[3] ",
                      self.driver)

    ############################selecting item drop down #######################################################
    @property
    def second_authorization_permission_selecting_item_drop_down_third_time(self):
        return Button(By.XPATH,
                      " (//*[@class='widgetContainer']//*[@class='dijitReset dijitStretch xwt-IconDropDownButtonContents dijitDownArrowButton'])[3]",
                      self.driver)

    ###############################adding the security group #########################################################
    @property
    def second_authorization_permission_selecting_second_time_seurity_group(self):
        return Button(By.XPATH, " (//*[contains(text(),'Security Group')])[2] ", self.driver)

    ################### selecting the pci servers ########################################################3
    @property
    def second_authorization_permission_selecting_pci_servers(self):
        return Button(By.XPATH, " (//*[contains(text(),'PCI_Servers')])[1] ", self.driver)
        ########################## closing the athorization permission button ##################################################

    @property
    def closing_second_auhorization_drop_down(self):
        return Button(By.XPATH,
                      " (//*[@class='dijitReset dijitInline dijitArrowButtonInner tokenFieldExpand'])[9] ",
                      self.driver)

        ######################selecting the done button #############################################################################

    @property
    def second_authorization_done_button(self):
        return Button(By.XPATH, " (//*[contains(text(),'Done')])[3]", self.driver)





            ##############################################################################################################################
################################################################################################################################
##################################################################################################################################

    @property
    def submit_button(self):
        return Button(By.XPATH, ".//*[@id='policyGroupingSubmitBtn'] ",self.driver)










    #####################################page actionsss #######################################################################

    ############################################################################################################################
    ####################page actions########################################
    #############################################################################################################################



    def add_policy_sets_authentication_and_autherization(self, policy_name, policy_description,
                                       first_authentication_standard_rule1,
                                       authentication_secnd_rule,
                                       third_authentication_policy_rule_3,
                                       selecting_first_authorization_policy_rule,
                                       selecting_second_authorization_policy_rule2):

        self.wait_for_loader([self.policy_sets_add_button])
        self.policy_sets_add_button.click()
        time.sleep(2)

        self.policy_sets_add_button_dropdown_selection.click()
        time.sleep(2)

        self.first_edit_button.click()
        time.sleep(2)

        self.fill_policy_sets_authentication_and_autherization_form(policy_name, policy_description,
                                                  first_authentication_standard_rule1,
                                                  authentication_secnd_rule,
                                                  third_authentication_policy_rule_3,
                                                  selecting_first_authorization_policy_rule,
                                                  selecting_second_authorization_policy_rule2)

        time.sleep(3)

    def fill_policy_sets_authentication_and_autherization_form(self, policy_name, policy_description,
                                             first_authentication_standard_rule1,
                                             authentication_secnd_rule,
                                             third_authentication_policy_rule_3,
                                             selecting_first_authorization_policy_rule,
                                             selecting_second_authorization_policy_rule2):
        self.wait_for_loader([self.policy_name])
        self.policy_name.click()
        self.policy_name.send_text(policy_name)

        self.policy_description.click()
        self.policy_description.send_text(policy_description)

        self.policy_condition_drop_down.click()
        time.sleep(3)

        self.drop_down_selection.click()
        time.sleep(3)

        self.condition_name_dropdown1.click()
        time.sleep(3)

        self.compound_condition.click()
        time.sleep(3)

        self.compound_condition_selection.click()
        time.sleep(3)

        self.done_button.click()
        time.sleep(3)

        #############################first autherzation policy page actions #################################

        self.first_authentication_edit_button_dropdown.click()
        time.sleep(2)

        self.first_selcting_insert_new_row_above.click()
        time.sleep(2)

        self.first_authentication_standard_rule1.click()
        self.first_authentication_standard_rule1.send_text(first_authentication_standard_rule1)
        time.sleep(2)

        self.first_authentication_rule1_conditions_dropdown.click()
        time.sleep(2)

        self.first_authentication_selecting_existing_condition_from_library.click()
        time.sleep(2)

        self.first_authentication_condition_name_dropdown.click()
        time.sleep(2)

        self.first_authentication_selecting_compound_condition.click()
        time.sleep(2)

        self.first_authentication_selecting_condition_name.click()
        time.sleep(2)

        self.first_authentication_protocol_drop_down.click()
        time.sleep(2)

        self.first_authentication_allowed_protocol_drop_down.click()
        time.sleep(2)

        self.first_authentication_selecting_default_network_access_protocol.click()
        time.sleep(2)

        self.first_authentication_use_button_drop_down.click()
        time.sleep(2)

        self.first_authentication_identity_resourse_drop_down.click()
        time.sleep(2)

        self.first_authentication_selecting_identity_resourse.click()
        time.sleep(2)

        self.first_authentication_done_button.click()
        time.sleep(2)

        #####################second authentication policy page actions ##############################
        self.authentication_secnd_edit_drop_down.click()
        time.sleep(2)

        self.authentication_secnd_selecting_new_row_above.click()
        time.sleep(2)

        self.authentication_secnd_rule.click()
        self.authentication_secnd_rule.send_text(authentication_secnd_rule)
        time.sleep(2)

        self.authentication_secnd_condition_dropdown_button.click()
        time.sleep(2)

        self.authentication_secnd_seclecting_existing_condition.click()
        time.sleep(2)

        self.authentication_secnd_selecting_condition_name_drop_down_button.click()
        time.sleep(2)

        self.authentication_secnd_selecting_compound_condition.click()
        time.sleep(2)

        self.authentication_secnd_selecting_condition1.click()
        time.sleep(2)

        self.authentication_secnd_selecting_settings_drop_down_button.click()
        time.sleep(2)

        self.authentication_secnd_selecting_add_condition_from_library_button.click()
        time.sleep(2)

        self.authentication_secnd_selecting_AND_operater_drop_down.click()
        time.sleep(2)

        self.authentication_secnd_selecting_And_operater.click()
        time.sleep(2)

        self.authentication_secnd_selecting_condition2_drop_down_button.click()
        time.sleep(2)

        self.authenticaion_secnd_selecting_compound_condition.click()
        time.sleep(2)

        self.authentication_secnd_selecting_condition2.click()
        time.sleep(2)

        self.authentication_secnd_selecting_allow_protocols_drop_down.click()
        time.sleep(2)

        self.authentication_secnd_selecting_allow_protocols.click()
        time.sleep(2)

        self.authentication_secnd_selecting_default_network_access.click()
        time.sleep(2)

        self.authentication_secnd_selecting_inernal_users_drop_down.click()
        time.sleep(2)

        self.authentication_secnd_selecting_identity_sourse_drop_down.click()
        time.sleep(2)

        self.authentication_secnd_selecting_identity_sourse_list.click()
        time.sleep(2)

        self.authentication_secnd_selecting_done_button.click()
        time.sleep(2)

        ##########third authentication page actions ###################################################################


        self.third_authentication_edit_drop_down_button.click()
        time.sleep(2)

        self.third_authentication_selecting_insert_new_row_above.click()
        time.sleep(2)

        self.third_authentication_policy_rule_3.click()
        self.third_authentication_policy_rule_3.send_text(third_authentication_policy_rule_3)
        time.sleep(2)

        self.third_authentication_policy_conditions_dropdown.click()
        time.sleep(2)

        self.third_authentication_selecting_existing_condition_from_library.click()
        time.sleep(2)

        self.third_authentication_selecting_condotion_name.click()
        time.sleep(2)

        self.third_authentication_selecting_compound_condition.click()
        time.sleep(2)

        self.third_authentication_selecting_wireless_mab_condition.click()
        time.sleep(2)

        self.third_authentication_selecting_allow_protocols_drop_down_button.click()
        time.sleep(2)

        self.third_authentication_selecting_allowed_protocols.click()
        time.sleep(2)

        self.third_authentication_selecting_default_network_access.click()
        time.sleep(2)

        self.third_authentication_selectig_inernal_users_drop_down_button.click()
        time.sleep(2)

        self.third_authentication_selecting_identity_source_drop_down_button.click()
        time.sleep(2)

        self.third_authentication_selecting_portal_sequence_resourse_from_identity_resourse.click()
        time.sleep(2)

        self.third_authentication_selecting_done_button.click()
        time.sleep(2)


        self.minimizing_authentication_drop_down.click()
        time.sleep(2)




##########################autherization policy page actions###################################################################3
        self. selecting_first_authorization_policy_edit_button_dropdown.click()
        time.sleep(3)

        self. selecing_first_authorization_insert_new_row_above.click()
        time.sleep(3)

        self.selecting_first_authorization_policy_rule.click()
        self.selecting_first_authorization_policy_rule.send_text(selecting_first_authorization_policy_rule)
        time.sleep(3)

        self.first_authorization_groups_drop_down_button.click()
        time.sleep(3)

        self.first_authorization_any_drop_down_button.click()
        time.sleep(3)

        self.first_authorization_user_identity_groups.click()
        time.sleep(3)

        self.first_authorization_chaitu_user_identity_group.click()
        time.sleep(3)

        self.first_authorization_groups_drop_down_button_close.click()
        time.sleep(2)

        self.first_authorization_conditions_drop_down_button.click()
        time.sleep(3)
        """
        self.first_authorization_existing_condition_from_library.click()
        time.sleep(4)

        self. first_authorization_condition_name_drop_down.click()
        time.sleep(3)

        self.first_authorization_compound_condition.click()
        time.sleep(2)

        self.first_authorization_Guest_flow_condition.click()
        time.sleep(2)
        """
        self.first_authorization_conditions_drop_down_button_close.click()
        time.sleep(2)

        self.first_authorization_permissions_drop_down_buton.click()
        time.sleep(2)

        self.first_authorization_existing_condition_from_library.click()
        time.sleep(2)

        self.first_authorization_condition_name_drop_down.click()
        time.sleep(2)

        self.first_authorization_compound_condition.click()
        time.sleep(2)

        self.first_authorization_Guest_flow_condition.click()
        time.sleep(2)

        self.first_authorization_conditions_drop_down_button_close.click()
        time.sleep(2)

        self.first_authorization_permissions_drop_down_buton.click()
        time.sleep(2)

        self.first_authorization_item_drop_down.click()
        time.sleep(2)

        self.first_authorization_security_group.click()
        time.sleep(2)

        self.first_authorization_chaitureddy_security_group.click()
        time.sleep(2)

        self.first_authorization_policy_done_button.click()
        time.sleep(2)

        ######################second  authorization policy page actions ####################################################3
        self.selecting_second_authorization_policy_edit_button_dropdown.click()
        time.sleep(2)

        self.selecing_second_authorization_insert_new_row_above.click()
        time.sleep(2)

        self.selecting_second_authorization_policy_rule2.click()
        self.selecting_second_authorization_policy_rule2.send_text(selecting_second_authorization_policy_rule2)
        time.sleep(2)

        self.second_authorization_groups_drop_down_button.click()
        time.sleep(2)

        self.second_authorization_any_drop_down_button.click()
        time.sleep(2)

        self.second_authorization_user_identity_groups.click()
        time.sleep(2)

        self.second_authorization_base_onboard_posture_group.click()
        time.sleep(2)

        self.second_authorization_plus_button_for_second_group.click()
        time.sleep(3)

        self.second_authorization_second_drop_down_for_group.click()
        time.sleep(3)

        self.second_authorization_end_point_identity_group.click()
        time.sleep(2)

        self.second_authorization_registerd_devices.click()
        time.sleep(2)

        self.second_authorization_groups_drop_down_close_button.click()
        time.sleep(2)

        self.second_authorization_condition_drop_down.click()
        time.sleep(2)

        self.second_authorization_permision_drop_down_button.click()
        time.sleep(1)

        self.second_authorization_condition_drop_down.click()
        time.sleep(2)

        self.second_authorization_existing_condition_from_library.click()
        time.sleep(1)

        self.second_authorization_condition_name_drop_down.click()
        time.sleep(1)

        self.second_authorization_compound_condition.click()
        time.sleep(1)

        self.second_authorization_EAP_TLS_condition.click()
        time.sleep(1)

        self.second_authorization_setting_button_for_adding_second_condition.click()
        time.sleep(1)

        self.second_authorization_add_condition_from_library.click()
        time.sleep(1)

        self.second_authorization_condition_2_name_drop_down.click()
        time.sleep(1)

        self.second_authorization_condition_2_simple_condition.click()
        time.sleep(1)

        self.second_authorization_condition_2_CertRenewalRequired.click()
        time.sleep(1)

        self.second_authorization_settings_buttons_for_adding_third_condition.click()
        time.sleep(1)

        self.second_authorization_conditon_3_add_condition_from_library.click()
        time.sleep(1)

        self.second_authorization_condition_3_name_drop_down.click()
        time.sleep(1)

        self.second_authorization_condition_3_compound_condition.click()
        time.sleep(1)

        self.second_authorization_condition_3_EAP_MSCHAP.click()
        time.sleep(1)

        self.second_authorization_condition_drop_down.click()
        time.sleep(2)

        self.second_authorization_permision_drop_down_button.click()
        time.sleep(3)

        self.second_authorization_permission_selecting_item_drop_down.click()
        time.sleep(2)

        self.second_authorization_permission_selecting_security_group.click()
        time.sleep(1)

        self.second_authorization_permission_selecting_network_access_permission.click()
        time.sleep(1)

        self.second_authorization_permission_selecting_plus_buuton_for_ading_second_permission.click()
        time.sleep(1)

        self.second_authorization_permission_selecting_item_drop_down_second_time.click()
        time.sleep(1)

        self.second_authorization_permission_selecting_standard_profile.click()
        time.sleep(1)

        self.second_authorization_permission_selecting_permit_access.click()
        time.sleep(1)

        self.second_authorization_permission_selecting_plus_buuton_for_ading_third_permission.click()
        time.sleep(1)

        self.second_authorization_permission_selecting_item_drop_down_third_time.click()
        time.sleep(1)

        self.second_authorization_permission_selecting_second_time_seurity_group.click()
        time.sleep(1)

        self.second_authorization_permission_selecting_pci_servers.click()
        time.sleep(1)

        self.closing_second_auhorization_drop_down.click()
        time.sleep(1)

        self.second_authorization_done_button.click()
        time.sleep(1)


        self.submit_button.scroll_to_element()
        self.submit_button.click()
        time.sleep(2)