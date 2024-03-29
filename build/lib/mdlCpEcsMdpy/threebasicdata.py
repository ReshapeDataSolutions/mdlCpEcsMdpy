import pymssql
from pyrda.dbms.rds import RdClient
# class NOAccount():
#
#     def __init__(self):
#         # 连接数据库
#         self.app3 = RdClient(token='9B6F803F-9D37-41A2-BDA0-70A7179AF0F3')
#
#     def update_RDS_ECS_ODS_BD_CUSTOMER(self):
#         """
#             ECS客户同步
#         """
#         # ECS客户同步
#         insert_into_RDS_ECS_ODS_BD_CUSTOMER_sql = """
#                                    INSERT INTO  RDS_ECS_ODS_BD_CUSTOMER
#                                     SELECT [FInterId]
#                                           ,[FApplyOrgName]
#                                           ,[FApplyDeptName]
#                                           ,[FApplierName]
#                                           ,[FDate]
#                                           ,[FNumber]
#                                           ,[FName]
#                                           ,[FShortName]
#                                           ,[FCOUNTRY]
#                                           ,[FPROVINCIAL]
#                                           ,[FTEL]
#                                           ,[FINVOICETITLE]
#                                           ,[FTAXREGISTERCODE]
#                                           ,[FBankName]
#                                           ,[FINVOICETEL]
#                                           ,[FAccountNumber]
#                                           ,[FINVOICEADDRESS]
#                                           ,[FINVOICETYPE]
#                                           ,[FTaxRate]
#                                           ,[FCONTACT]
#                                           ,[FBizAddress]
#                                           ,[FMOBILE]
#                                           ,[FSalesman]
#                                           ,[FAalesDeptName]
#                                           ,[FCustTypeNo]
#                                           ,[FGroupNo]
#                                           ,[F_SZSP_KHFLNo]
#                                           ,[FSalesGroupNo]
#                                           ,[FTRADINGCURRNO]
#                                           ,[FSETTLETYPENO]
#                                           ,[FRECCONDITIONNO]
#                                           ,[FPRICELISTNO]
#                                           ,[FUploadDate]
#                                           ,[FIsdo]
#                                           ,[F_SZSP_BLOCNAME]
#                                           ,[F_SZSP_KHZYJBNo]
#                                           ,[F_SZSP_KHGHSXNo]
#                                           ,[F_SZSP_XSMSNo]
#                                           ,[F_SZSP_XSMSSXNo]
#                                           ,[F_SZSP_Text]
#                                       FROM [cprds].[dbo].[RDS_ECS_SRC_BD_CUSTOMER]
#                                       WHERE  FNumber NOT IN
#                                       ( SELECT  FNumber FROM RDS_ECS_ODS_BD_CUSTOMER )
#                            """
#
#         res=self.app3.update(insert_into_RDS_ECS_ODS_BD_CUSTOMER_sql)
#         # self.new_cursor.execute(insert_into_RDS_ECS_ODS_BD_CUSTOMER_sql)
#         # res = self.new_con.commit()
#         return res
#
#     def update_RDS_ECS_ODS_bd_MaterialDetail(self):
#         """
#             ECS物料同步
#         """
#         # ECS物料同步
#         insert_into_RDS_ECS_ODS_bd_MaterialDetail_sql = """
#                         INSERT INTO  RDS_ECS_ODS_bd_MaterialDetail
#                         SELECT  [FInterId]
#                           ,[FDeptId]
#                           ,[FUserId]
#                           ,[FApplyOrgName]
#                           ,[FVarDateTime]
#                           ,[FNumber]
#                           ,[FName]
#                           ,[FSpecification]
#                           ,[FDescription]
#                           ,[FTaxRateId]
#                           ,[FGROSSWEIGHT]
#                           ,[FNETWEIGHT]
#                           ,[FLENGTH]
#                           ,[FWIDTH]
#                           ,[FHEIGHT]
#                           ,[FVOLUME]
#                           ,[FSafeStock]
#                           ,[FMinPackCount]
#                           ,[FPlanningStrategy]
#                           ,[FOrderPolicy]
#                           ,[FFixLeadTime]
#                           ,[FFixLeadTimeType]
#                           ,[FVarLeadTime]
#                           ,[FVarLeadTimeType]
#                           ,[FOrderIntervalTimeType]
#                           ,[FOrderIntervalTime]
#                           ,[FMaxPOQty]
#                           ,[FMinPOQty]
#                           ,[FIncreaseQty]
#                           ,[FEOQ]
#                           ,[FVarLeadTimeLotSize]
#                           ,[FFinishReceiptOverRate]
#                           ,[FFinishReceiptShortRate]
#                           ,[FMinIssueQty]
#                           ,[F_SZSP_CheckBox]
#                           ,[FISMinIssueQty]
#                           ,[FIsBatchManage]
#                           ,[FOverControlMode]
#                           ,[FIsKFPeriod]
#                           ,[FCheckOut]
#                           ,[FMaterialGroup]
#                           ,[FErpClsID]
#                           ,[FCategoryID]
#                           ,[FTaxCategoryCodeId]
#                           ,[FWEIGHTUNITID]
#                           ,[FBaseUnitId]
#                           ,[FVOLUMEUNITID]
#                           ,[FBatchRuleID]
#                           ,[F_SZSP_Assistant]
#                           ,[FUploadDate]
#                           ,[Fisdo]
#                           ,[FChecker]
#                           ,[FOldNumber]
#                           ,[FIsPurchase]
#                           ,[F_SZSP_Decimal]
#                           ,[F_SZSP_Decimal1]
#                           ,[F_SZSP_SKUnumber]
#                           ,[F_SZSP_PackCoefficient]
#                           ,[FExpUnit]
#                           ,[FExpPeriod]
#                           ,[FIsEnableSafeStock]
#                           ,[FIsEnableMinStock]
#                           ,[FMinStock]
#                           ,[FIsEnableMaxStock]
#                           ,[FMaxStock]
#                           ,[F_SZSP_Itemnumber]
#                           ,[FBaseProperty]
#                           ,[FSupplierMaterialCode]
#                           ,[FMaterialGroupName]
#                           ,[FMaterialGroupCode]
#                           ,[FParentMaterialGroupCode]
#                           ,[FParentMaterialGroupName]
#                           FROM RDS_ECS_SRC_bd_MaterialDetail  A
#                                where not exists
#                             ( select * from RDS_ECS_ODS_bd_MaterialDetail B
#                             where  A.[FInterId] =B.[FInterId]
#                             AND A.[FNumber]= B.[FNumber])
#                 """
#
#         res = self.app3.update(insert_into_RDS_ECS_ODS_bd_MaterialDetail_sql)
#         # self.new_cursor.execute(insert_into_RDS_ECS_ODS_bd_MaterialDetail_sql)
#         # res = self.new_con.commit()
#         return res
#
#     def update_RDS_ECS_ODS_bd_SupplierDetail(self):
#         """
#             ECS供应商同步
#         """
#         # ECS供应商同步
#         insert_into_RDS_ECS_ODS_bd_SupplierDetail_sql = """
#
#                         INSERT INTO  RDS_ECS_ODS_bd_SupplierDetail
#
#                             SELECT [FInterId]
#                                   ,[FApplyOrgName]
#                                   ,[FApplyDeptName]
#                                   ,[FApplierName]
#                                   ,[FDate]
#                                   ,[FNumber]
#                                   ,[FName]
#                                   ,[FShortName]
#                                   ,[FCountry]
#                                   ,[FProvince]
#                                   ,[FZipCode]
#                                   ,[FUniversalCode]
#                                   ,[FRegisterAddress]
#                                   ,[FMngrDeptName]
#                                   ,[FMngrMan]
#                                   ,[FSullierType]
#                                   ,[FInvoiceType]
#                                   ,[FTaxRate]
#                                   ,[FAccountNumber]
#                                   ,[FAccountName]
#                                   ,[FBankTransferCode]
#                                   ,[FBankName]
#                                   ,[FBankAddr]
#                                   ,[FContact]
#                                   ,[FMobile]
#                                   ,[FEMail]
#                                   ,[FSupplierCategoryNo]
#                                   ,[FSupplierGradeNo]
#                                   ,[FPriceListNo]
#                                   ,[FSettleCurrencyNo]
#                                   ,[FSettlementMethodNo]
#                                   ,[FPaymentConditionNo]
#                                   ,[FCurrencyNo]
#                                   ,[FUploadDate]
#                                   ,[Fisdo]
#                                   ,[FPurchaserGroupId]
#                               FROM RDS_ECS_SRC_bd_SupplierDetail A
#                                where not exists
#                             (SELECT * FROM RDS_ECS_ODS_bd_SupplierDetail  B
#                             WHERE  A.FNumber = B.FNumber )
#
#
#                 """
#
#         res = self.app3.update(insert_into_RDS_ECS_ODS_bd_SupplierDetail_sql)
#         # self.new_cursor.execute(insert_into_RDS_ECS_ODS_bd_SupplierDetail_sql)
#         # res = self.new_con.commit()
#         return res



def NOAccount(FToken):

    app3=RdClient(token=FToken)

    insert_into_RDS_ECS_ODS_BD_CUSTOMER_sql = """
                                       INSERT INTO  RDS_ECS_ODS_BD_CUSTOMER
                                        SELECT [FInterId]
                                              ,[FApplyOrgName]
                                              ,[FApplyDeptName]
                                              ,[FApplierName]
                                              ,[FDate]
                                              ,[FNumber]
                                              ,[FName]
                                              ,[FShortName]
                                              ,[FCOUNTRY]
                                              ,[FPROVINCIAL]
                                              ,[FTEL]
                                              ,[FINVOICETITLE]
                                              ,[FTAXREGISTERCODE]
                                              ,[FBankName]
                                              ,[FINVOICETEL]
                                              ,[FAccountNumber]
                                              ,[FINVOICEADDRESS]
                                              ,[FINVOICETYPE]
                                              ,[FTaxRate]
                                              ,[FCONTACT]
                                              ,[FBizAddress]
                                              ,[FMOBILE]
                                              ,[FSalesman]
                                              ,[FAalesDeptName]
                                              ,[FCustTypeNo]
                                              ,[FGroupNo]
                                              ,[F_SZSP_KHFLNo]
                                              ,[FSalesGroupNo]
                                              ,[FTRADINGCURRNO]
                                              ,[FSETTLETYPENO]
                                              ,[FRECCONDITIONNO]
                                              ,[FPRICELISTNO]
                                              ,[FUploadDate]
                                              ,[FIsdo]
                                              ,[F_SZSP_BLOCNAME]
                                              ,[F_SZSP_KHZYJBNo]
                                              ,[F_SZSP_KHGHSXNo]
                                              ,[F_SZSP_XSMSNo]
                                              ,[F_SZSP_XSMSSXNo]
                                              ,[F_SZSP_Text]
                                          FROM [cprds].[dbo].[RDS_ECS_SRC_BD_CUSTOMER]
                                          WHERE  FNumber NOT IN
                                          ( SELECT  FNumber FROM RDS_ECS_ODS_BD_CUSTOMER )
                               """

    app3.update(insert_into_RDS_ECS_ODS_BD_CUSTOMER_sql)

    insert_into_RDS_ECS_ODS_bd_MaterialDetail_sql = """
                            INSERT INTO  RDS_ECS_ODS_bd_MaterialDetail
                            SELECT  [FInterId]
                              ,[FDeptId]
                              ,[FUserId]
                              ,[FApplyOrgName]
                              ,[FVarDateTime]
                              ,[FNumber]
                              ,[FName]
                              ,[FSpecification]
                              ,[FDescription]
                              ,[FTaxRateId]
                              ,[FGROSSWEIGHT]
                              ,[FNETWEIGHT]
                              ,[FLENGTH]
                              ,[FWIDTH]
                              ,[FHEIGHT]
                              ,[FVOLUME]
                              ,[FSafeStock]
                              ,[FMinPackCount]
                              ,[FPlanningStrategy]
                              ,[FOrderPolicy]
                              ,[FFixLeadTime]
                              ,[FFixLeadTimeType]
                              ,[FVarLeadTime]
                              ,[FVarLeadTimeType]
                              ,[FOrderIntervalTimeType]
                              ,[FOrderIntervalTime]
                              ,[FMaxPOQty]
                              ,[FMinPOQty]
                              ,[FIncreaseQty]
                              ,[FEOQ]
                              ,[FVarLeadTimeLotSize]
                              ,[FFinishReceiptOverRate]
                              ,[FFinishReceiptShortRate]
                              ,[FMinIssueQty]
                              ,[F_SZSP_CheckBox]
                              ,[FISMinIssueQty]
                              ,[FIsBatchManage]
                              ,[FOverControlMode]
                              ,[FIsKFPeriod]
                              ,[FCheckOut]
                              ,[FMaterialGroup]
                              ,[FErpClsID]
                              ,[FCategoryID]
                              ,[FTaxCategoryCodeId]
                              ,[FWEIGHTUNITID]
                              ,[FBaseUnitId]
                              ,[FVOLUMEUNITID]
                              ,[FBatchRuleID]
                              ,[F_SZSP_Assistant]
                              ,[FUploadDate]
                              ,[Fisdo]
                              ,[FChecker]
                              ,[FOldNumber]
                              ,[FIsPurchase]
                              ,[F_SZSP_Decimal]
                              ,[F_SZSP_Decimal1]
                              ,[F_SZSP_SKUnumber]
                              ,[F_SZSP_PackCoefficient]
                              ,[FExpUnit]
                              ,[FExpPeriod]
                              ,[FIsEnableSafeStock]
                              ,[FIsEnableMinStock]
                              ,[FMinStock]
                              ,[FIsEnableMaxStock]
                              ,[FMaxStock]
                              ,[F_SZSP_Itemnumber]
                              ,[FBaseProperty]
                              ,[FSupplierMaterialCode]
                              ,[FMaterialGroupName]
                              ,[FMaterialGroupCode]
                              ,[FParentMaterialGroupCode]
                              ,[FParentMaterialGroupName]
                              FROM RDS_ECS_SRC_bd_MaterialDetail  A
                                   where not exists
                                ( select * from RDS_ECS_ODS_bd_MaterialDetail B
                                where  A.[FInterId] =B.[FInterId]
                                AND A.[FNumber]= B.[FNumber])
                    """

    app3.update(insert_into_RDS_ECS_ODS_bd_MaterialDetail_sql)

    insert_into_RDS_ECS_ODS_bd_SupplierDetail_sql = """

                            INSERT INTO  RDS_ECS_ODS_bd_SupplierDetail

                                SELECT [FInterId]
                                      ,[FApplyOrgName]
                                      ,[FApplyDeptName]
                                      ,[FApplierName]
                                      ,[FDate]
                                      ,[FNumber]
                                      ,[FName]
                                      ,[FShortName]
                                      ,[FCountry]
                                      ,[FProvince]
                                      ,[FZipCode]
                                      ,[FUniversalCode]
                                      ,[FRegisterAddress]
                                      ,[FMngrDeptName]
                                      ,[FMngrMan]
                                      ,[FSullierType]
                                      ,[FInvoiceType]
                                      ,[FTaxRate]
                                      ,[FAccountNumber]
                                      ,[FAccountName]
                                      ,[FBankTransferCode]
                                      ,[FBankName]
                                      ,[FBankAddr]
                                      ,[FContact]
                                      ,[FMobile]
                                      ,[FEMail]
                                      ,[FSupplierCategoryNo]
                                      ,[FSupplierGradeNo]
                                      ,[FPriceListNo]
                                      ,[FSettleCurrencyNo]
                                      ,[FSettlementMethodNo]
                                      ,[FPaymentConditionNo]
                                      ,[FCurrencyNo]
                                      ,[FUploadDate]
                                      ,[Fisdo]
                                      ,[FPurchaserGroupId]
                                  FROM RDS_ECS_SRC_bd_SupplierDetail A
                                   where not exists
                                (SELECT * FROM RDS_ECS_ODS_bd_SupplierDetail  B
                                WHERE  A.FNumber = B.FNumber )


                    """

    app3.update(insert_into_RDS_ECS_ODS_bd_SupplierDetail_sql)


