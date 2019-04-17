import simplefix

SENDER_COMP_ID = "COEP_Credit_Suisse"

components_names=["CommissionData","DiscretionInstructions","FinancingDetails","Instrument","InstrumentExtension","InstrumentLeg","LegBenchmarkCurveData","LegStipulations","NestedParties","OrderQtyData","Parties","PegInstructions","PositionAmountData","PositionQty","SettlInstructionsData","SettlParties","SpreadOrBenchmarkCurveData","Stipulations","TrdRegTimestamps","UnderlyingInstrument","YieldData","UnderlyingStipulations","NestedParties2","NestedParties3","AffectedOrdGrp","AllocAckGrp","AllocGrp","BidCompReqGrp","BidCompRspGrp","BidDescReqGrp","ClrInstGrp","CollInqQualGrp","CompIDReqGrp","CompIDStatGrp","ContAmtGrp","ContraGrp","CpctyConfGrp","ExecAllocGrp","ExecCollGrp","ExecsGrp","InstrmtGrp","InstrmtLegExecGrp","InstrmtLegGrp","InstrmtLegIOIGrp","InstrmtLegSecListGrp","InstrmtMDReqGrp","InstrmtStrkPxGrp","IOIQualGrp","LegOrdGrp","LegPreAllocGrp","LegQuotGrp","LegQuotStatGrp","LinesOfTextGrp","ListOrdGrp","MDFullGrp","MDIncGrp","MDReqGrp","MDRjctGrp","MiscFeesGrp","OrdAllocGrp","OrdListStatGrp","PosUndInstrmtGrp","PreAllocGrp","PreAllocMlegGrp","QuotCxlEntriesGrp","QuotEntryAckGrp","QuotEntryGrp","QuotQualGrp","QuotReqGrp","QuotReqLegsGrp","QuotReqRjctGrp","QuotSetAckGrp","QuotSetGrp","RelSymDerivSecGrp","RFQReqGrp","RgstDistInstGrp","RgstDtlsGrp","RoutingGrp","SecListGrp","SecTypesGrp","SettlInstGrp","SideCrossOrdCxlGrp","SideCrossOrdModGrp","TrdAllocGrp","TrdCapRptSideGrp","TrdCollGrp","TrdInstrmtLegGrp","TrdgSesGrp","UndInstrmtCollGrp","UndInstrmtGrp","UndInstrmtStrkPxGrp","TrdCapDtGrp","EvntGrp","SecAltIDGrp","LegSecAltIDGrp","UndSecAltIDGrp","AttrbGrp","DlvyInstGrp","SettlPtysSubGrp","PtysSubGrp","NstdPtysSubGrp","NstdPtys2SubGrp","NstdPtys3SubGrp"]

tag_name_to_num={"Account":1,"AdvId":2,"AdvRefID":3,"AdvSide":4,"AdvTransType":5,"AvgPx":6,"BeginSeqNo":7,"BeginString":8,"BodyLength":9,"CheckSum":10,"ClOrdID":11,"Commission":12,"CommType":13,"CumQty":14,"Currency":15,"EndSeqNo":16,"ExecID":17,"ExecInst":18,"ExecRefID":19,"HandlInst":21,"SecurityIDSource":22,"IOIID":23,"IOIQltyInd":25,"IOIRefID":26,"IOIQty":27,"IOITransType":28,"LastCapacity":29,"LastMkt":30,"LastPx":31,"LastQty":32,"NoLinesOfText":33,"MsgSeqNum":34,"MsgType":35,"NewSeqNo":36,"OrderID":37,"OrderQty":38,"OrdStatus":39,"OrdType":40,"OrigClOrdID":41,"OrigTime":42,"PossDupFlag":43,"Price":44,"RefSeqNum":45,"SecurityID":48,"SenderCompID":49,"SenderSubID":50,"SendingTime":52,"Quantity":53,"Side":54,"Symbol":55,"TargetCompID":56,"TargetSubID":57,"Text":58,"TimeInForce":59,"TransactTime":60,"Urgency":61,"ValidUntilTime":62,"SettlType":63,"SettlDate":64,"SymbolSfx":65,"ListID":66,"ListSeqNo":67,"TotNoOrders":68,"ListExecInst":69,"AllocID":70,"AllocTransType":71,"RefAllocID":72,"NoOrders":73,"AvgPxPrecision":74,"TradeDate":75,"PositionEffect":77,"NoAllocs":78,"AllocAccount":79,"AllocQty":80,"ProcessCode":81,"NoRpts":82,"RptSeq":83,"CxlQty":84,"NoDlvyInst":85,"AllocStatus":87,"AllocRejCode":88,"Signature":89,"SecureDataLen":90,"SecureData":91,"SignatureLength":93,"EmailType":94,"RawDataLength":95,"RawData":96,"PossResend":97,"EncryptMethod":98,"StopPx":99,"ExDestination":100,"CxlRejReason":102,"OrdRejReason":103,"IOIQualifier":104,"Issuer":106,"SecurityDesc":107,"HeartBtInt":108,"MinQty":110,"MaxFloor":111,"TestReqID":112,"ReportToExch":113,"LocateReqd":114,"OnBehalfOfCompID":115,"OnBehalfOfSubID":116,"QuoteID":117,"NetMoney":118,"SettlCurrAmt":119,"SettlCurrency":120,"ForexReq":121,"OrigSendingTime":122,"GapFillFlag":123,"NoExecs":124,"ExpireTime":126,"DKReason":127,"DeliverToCompID":128,"DeliverToSubID":129,"IOINaturalFlag":130,"QuoteReqID":131,"BidPx":132,"OfferPx":133,"BidSize":134,"OfferSize":135,"NoMiscFees":136,"MiscFeeAmt":137,"MiscFeeCurr":138,"MiscFeeType":139,"PrevClosePx":140,"ResetSeqNumFlag":141,"SenderLocationID":142,"TargetLocationID":143,"OnBehalfOfLocationID":144,"DeliverToLocationID":145,"NoRelatedSym":146,"Subject":147,"Headline":148,"URLLink":149,"ExecType":150,"LeavesQty":151,"CashOrderQty":152,"AllocAvgPx":153,"AllocNetMoney":154,"SettlCurrFxRate":155,"SettlCurrFxRateCalc":156,"NumDaysInterest":157,"AccruedInterestRate":158,"AccruedInterestAmt":159,"SettlInstMode":160,"AllocText":161,"SettlInstID":162,"SettlInstTransType":163,"EmailThreadID":164,"SettlInstSource":165,"SecurityType":167,"EffectiveTime":168,"StandInstDbType":169,"StandInstDbName":170,"StandInstDbID":171,"SettlDeliveryType":172,"BidSpotRate":188,"BidForwardPoints":189,"OfferSpotRate":190,"OfferForwardPoints":191,"OrderQty2":192,"SettlDate2":193,"LastSpotRate":194,"LastForwardPoints":195,"AllocLinkID":196,"AllocLinkType":197,"SecondaryOrderID":198,"NoIOIQualifiers":199,"MaturityMonthYear":200,"PutOrCall":201,"StrikePrice":202,"CoveredOrUncovered":203,"OptAttribute":206,"SecurityExchange":207,"NotifyBrokerOfCredit":208,"AllocHandlInst":209,"MaxShow":210,"PegOffsetValue":211,"XmlDataLen":212,"XmlData":213,"SettlInstRefID":214,"NoRoutingIDs":215,"RoutingType":216,"RoutingID":217,"Spread":218,"BenchmarkCurveCurrency":220,"BenchmarkCurveName":221,"BenchmarkCurvePoint":222,"CouponRate":223,"CouponPaymentDate":224,"IssueDate":225,"RepurchaseTerm":226,"RepurchaseRate":227,"Factor":228,"TradeOriginationDate":229,"ExDate":230,"ContractMultiplier":231,"NoStipulations":232,"StipulationType":233,"StipulationValue":234,"YieldType":235,"Yield":236,"TotalTakedown":237,"Concession":238,"RepoCollateralSecurityType":239,"RedemptionDate":240,"UnderlyingCouponPaymentDate":241,"UnderlyingIssueDate":242,"UnderlyingRepoCollateralSecurityType":243,"UnderlyingRepurchaseTerm":244,"UnderlyingRepurchaseRate":245,"UnderlyingFactor":246,"UnderlyingRedemptionDate":247,"LegCouponPaymentDate":248,"LegIssueDate":249,"LegRepoCollateralSecurityType":250,"LegRepurchaseTerm":251,"LegRepurchaseRate":252,"LegFactor":253,"LegRedemptionDate":254,"CreditRating":255,"UnderlyingCreditRating":256,"LegCreditRating":257,"TradedFlatSwitch":258,"BasisFeatureDate":259,"BasisFeaturePrice":260,"MDReqID":262,"SubscriptionRequestType":263,"MarketDepth":264,"MDUpdateType":265,"AggregatedBook":266,"NoMDEntryTypes":267,"NoMDEntries":268,"MDEntryType":269,"MDEntryPx":270,"MDEntrySize":271,"MDEntryDate":272,"MDEntryTime":273,"TickDirection":274,"MDMkt":275,"QuoteCondition":276,"TradeCondition":277,"MDEntryID":278,"MDUpdateAction":279,"MDEntryRefID":280,"MDReqRejReason":281,"MDEntryOriginator":282,"LocationID":283,"DeskID":284,"DeleteReason":285,"OpenCloseSettlFlag":286,"SellerDays":287,"MDEntryBuyer":288,"MDEntrySeller":289,"MDEntryPositionNo":290,"FinancialStatus":291,"CorporateAction":292,"DefBidSize":293,"DefOfferSize":294,"NoQuoteEntries":295,"NoQuoteSets":296,"QuoteStatus":297,"QuoteCancelType":298,"QuoteEntryID":299,"QuoteRejectReason":300,"QuoteResponseLevel":301,"QuoteSetID":302,"QuoteRequestType":303,"TotNoQuoteEntries":304,"UnderlyingSecurityIDSource":305,"UnderlyingIssuer":306,"UnderlyingSecurityDesc":307,"UnderlyingSecurityExchange":308,"UnderlyingSecurityID":309,"UnderlyingSecurityType":310,"UnderlyingSymbol":311,"UnderlyingSymbolSfx":312,"UnderlyingMaturityMonthYear":313,"UnderlyingPutOrCall":315,"UnderlyingStrikePrice":316,"UnderlyingOptAttribute":317,"UnderlyingCurrency":318,"SecurityReqID":320,"SecurityRequestType":321,"SecurityResponseID":322,"SecurityResponseType":323,"SecurityStatusReqID":324,"UnsolicitedIndicator":325,"SecurityTradingStatus":326,"HaltReasonChar":327,"InViewOfCommon":328,"DueToRelated":329,"BuyVolume":330,"SellVolume":331,"HighPx":332,"LowPx":333,"Adjustment":334,"TradSesReqID":335,"TradingSessionID":336,"ContraTrader":337,"TradSesMethod":338,"TradSesMode":339,"TradSesStatus":340,"TradSesStartTime":341,"TradSesOpenTime":342,"TradSesPreCloseTime":343,"TradSesCloseTime":344,"TradSesEndTime":345,"NumberOfOrders":346,"MessageEncoding":347,"EncodedIssuerLen":348,"EncodedIssuer":349,"EncodedSecurityDescLen":350,"EncodedSecurityDesc":351,"EncodedListExecInstLen":352,"EncodedListExecInst":353,"EncodedTextLen":354,"EncodedText":355,"EncodedSubjectLen":356,"EncodedSubject":357,"EncodedHeadlineLen":358,"EncodedHeadline":359,"EncodedAllocTextLen":360,"EncodedAllocText":361,"EncodedUnderlyingIssuerLen":362,"EncodedUnderlyingIssuer":363,"EncodedUnderlyingSecurityDescLen":364,"EncodedUnderlyingSecurityDesc":365,"AllocPrice":366,"QuoteSetValidUntilTime":367,"QuoteEntryRejectReason":368,"LastMsgSeqNumProcessed":369,"RefTagID":371,"RefMsgType":372,"SessionRejectReason":373,"BidRequestTransType":374,"ContraBroker":375,"ComplianceID":376,"SolicitedFlag":377,"ExecRestatementReason":378,"BusinessRejectRefID":379,"BusinessRejectReason":380,"GrossTradeAmt":381,"NoContraBrokers":382,"MaxMessageSize":383,"NoMsgTypes":384,"MsgDirection":385,"NoTradingSessions":386,"TotalVolumeTraded":387,"DiscretionInst":388,"DiscretionOffsetValue":389,"BidID":390,"ClientBidID":391,"ListName":392,"TotNoRelatedSym":393,"BidType":394,"NumTickets":395,"SideValue1":396,"SideValue2":397,"NoBidDescriptors":398,"BidDescriptorType":399,"BidDescriptor":400,"SideValueInd":401,"LiquidityPctLow":402,"LiquidityPctHigh":403,"LiquidityValue":404,"EFPTrackingError":405,"FairValue":406,"OutsideIndexPct":407,"ValueOfFutures":408,"LiquidityIndType":409,"WtAverageLiquidity":410,"ExchangeForPhysical":411,"OutMainCntryUIndex":412,"CrossPercent":413,"ProgRptReqs":414,"ProgPeriodInterval":415,"IncTaxInd":416,"NumBidders":417,"BidTradeType":418,"BasisPxType":419,"NoBidComponents":420,"Country":421,"TotNoStrikes":422,"PriceType":423,"DayOrderQty":424,"DayCumQty":425,"DayAvgPx":426,"GTBookingInst":427,"NoStrikes":428,"ListStatusType":429,"NetGrossInd":430,"ListOrderStatus":431,"ExpireDate":432,"ListExecInstType":433,"CxlRejResponseTo":434,"UnderlyingCouponRate":435,"UnderlyingContractMultiplier":436,"ContraTradeQty":437,"ContraTradeTime":438,"LiquidityNumSecurities":441,"MultiLegReportingType":442,"StrikeTime":443,"ListStatusText":444,"EncodedListStatusTextLen":445,"EncodedListStatusText":446,"PartyIDSource":447,"PartyID":448,"NetChgPrevDay":451,"PartyRole":452,"NoPartyIDs":453,"NoSecurityAltID":454,"SecurityAltID":455,"SecurityAltIDSource":456,"NoUnderlyingSecurityAltID":457,"UnderlyingSecurityAltID":458,"UnderlyingSecurityAltIDSource":459,"Product":460,"CFICode":461,"UnderlyingProduct":462,"UnderlyingCFICode":463,"TestMessageIndicator":464,"BookingRefID":466,"IndividualAllocID":467,"RoundingDirection":468,"RoundingModulus":469,"CountryOfIssue":470,"StateOrProvinceOfIssue":471,"LocaleOfIssue":472,"NoRegistDtls":473,"MailingDtls":474,"InvestorCountryOfResidence":475,"PaymentRef":476,"DistribPaymentMethod":477,"CashDistribCurr":478,"CommCurrency":479,"CancellationRights":480,"MoneyLaunderingStatus":481,"MailingInst":482,"TransBkdTime":483,"ExecPriceType":484,"ExecPriceAdjustment":485,"DateOfBirth":486,"TradeReportTransType":487,"CardHolderName":488,"CardNumber":489,"CardExpDate":490,"CardIssNum":491,"PaymentMethod":492,"RegistAcctType":493,"Designation":494,"TaxAdvantageType":495,"RegistRejReasonText":496,"FundRenewWaiv":497,"CashDistribAgentName":498,"CashDistribAgentCode":499,"CashDistribAgentAcctNumber":500,"CashDistribPayRef":501,"CashDistribAgentAcctName":502,"CardStartDate":503,"PaymentDate":504,"PaymentRemitterID":505,"RegistStatus":506,"RegistRejReasonCode":507,"RegistRefID":508,"RegistDtls":509,"NoDistribInsts":510,"RegistEmail":511,"DistribPercentage":512,"RegistID":513,"RegistTransType":514,"ExecValuationPoint":515,"OrderPercent":516,"OwnershipType":517,"NoContAmts":518,"ContAmtType":519,"ContAmtValue":520,"ContAmtCurr":521,"OwnerType":522,"PartySubID":523,"NestedPartyID":524,"NestedPartyIDSource":525,"SecondaryClOrdID":526,"SecondaryExecID":527,"OrderCapacity":528,"OrderRestrictions":529,"MassCancelRequestType":530,"MassCancelResponse":531,"MassCancelRejectReason":532,"TotalAffectedOrders":533,"NoAffectedOrders":534,"AffectedOrderID":535,"AffectedSecondaryOrderID":536,"QuoteType":537,"NestedPartyRole":538,"NoNestedPartyIDs":539,"TotalAccruedInterestAmt":540,"MaturityDate":541,"UnderlyingMaturityDate":542,"InstrRegistry":543,"CashMargin":544,"NestedPartySubID":545,"Scope":546,"MDImplicitDelete":547,"CrossID":548,"CrossType":549,"CrossPrioritization":550,"OrigCrossID":551,"NoSides":552,"Username":553,"Password":554,"NoLegs":555,"LegCurrency":556,"TotNoSecurityTypes":557,"NoSecurityTypes":558,"SecurityListRequestType":559,"SecurityRequestResult":560,"RoundLot":561,"MinTradeVol":562,"MultiLegRptTypeReq":563,"LegPositionEffect":564,"LegCoveredOrUncovered":565,"LegPrice":566,"TradSesStatusRejReason":567,"TradeRequestID":568,"TradeRequestType":569,"PreviouslyReported":570,"TradeReportID":571,"TradeReportRefID":572,"MatchStatus":573,"MatchType":574,"OddLot":575,"NoClearingInstructions":576,"ClearingInstruction":577,"TradeInputSource":578,"TradeInputDevice":579,"NoDates":580,"AccountType":581,"CustOrderCapacity":582,"ClOrdLinkID":583,"MassStatusReqID":584,"MassStatusReqType":585,"OrigOrdModTime":586,"LegSettlType":587,"LegSettlDate":588,"DayBookingInst":589,"BookingUnit":590,"PreallocMethod":591,"UnderlyingCountryOfIssue":592,"UnderlyingStateOrProvinceOfIssue":593,"UnderlyingLocaleOfIssue":594,"UnderlyingInstrRegistry":595,"LegCountryOfIssue":596,"LegStateOrProvinceOfIssue":597,"LegLocaleOfIssue":598,"LegInstrRegistry":599,"LegSymbol":600,"LegSymbolSfx":601,"LegSecurityID":602,"LegSecurityIDSource":603,"NoLegSecurityAltID":604,"LegSecurityAltID":605,"LegSecurityAltIDSource":606,"LegProduct":607,"LegCFICode":608,"LegSecurityType":609,"LegMaturityMonthYear":610,"LegMaturityDate":611,"LegStrikePrice":612,"LegOptAttribute":613,"LegContractMultiplier":614,"LegCouponRate":615,"LegSecurityExchange":616,"LegIssuer":617,"EncodedLegIssuerLen":618,"EncodedLegIssuer":619,"LegSecurityDesc":620,"EncodedLegSecurityDescLen":621,"EncodedLegSecurityDesc":622,"LegRatioQty":623,"LegSide":624,"TradingSessionSubID":625,"AllocType":626,"NoHops":627,"HopCompID":628,"HopSendingTime":629,"HopRefID":630,"MidPx":631,"BidYield":632,"MidYield":633,"OfferYield":634,"ClearingFeeIndicator":635,"WorkingIndicator":636,"LegLastPx":637,"PriorityIndicator":638,"PriceImprovement":639,"Price2":640,"LastForwardPoints2":641,"BidForwardPoints2":642,"OfferForwardPoints2":643,"RFQReqID":644,"MktBidPx":645,"MktOfferPx":646,"MinBidSize":647,"MinOfferSize":648,"QuoteStatusReqID":649,"LegalConfirm":650,"UnderlyingLastPx":651,"UnderlyingLastQty":652,"LegRefID":654,"ContraLegRefID":655,"SettlCurrBidFxRate":656,"SettlCurrOfferFxRate":657,"QuoteRequestRejectReason":658,"SideComplianceID":659,"AcctIDSource":660,"AllocAcctIDSource":661,"BenchmarkPrice":662,"BenchmarkPriceType":663,"ConfirmID":664,"ConfirmStatus":665,"ConfirmTransType":666,"ContractSettlMonth":667,"DeliveryForm":668,"LastParPx":669,"NoLegAllocs":670,"LegAllocAccount":671,"LegIndividualAllocID":672,"LegAllocQty":673,"LegAllocAcctIDSource":674,"LegSettlCurrency":675,"LegBenchmarkCurveCurrency":676,"LegBenchmarkCurveName":677,"LegBenchmarkCurvePoint":678,"LegBenchmarkPrice":679,"LegBenchmarkPriceType":680,"LegBidPx":681,"LegIOIQty":682,"NoLegStipulations":683,"LegOfferPx":684,"LegPriceType":686,"LegQty":687,"LegStipulationType":688,"LegStipulationValue":689,"LegSwapType":690,"Pool":691,"QuotePriceType":692,"QuoteRespID":693,"QuoteRespType":694,"QuoteQualifier":695,"YieldRedemptionDate":696,"YieldRedemptionPrice":697,"YieldRedemptionPriceType":698,"BenchmarkSecurityID":699,"ReversalIndicator":700,"YieldCalcDate":701,"NoPositions":702,"PosType":703,"LongQty":704,"ShortQty":705,"PosQtyStatus":706,"PosAmtType":707,"PosAmt":708,"PosTransType":709,"PosReqID":710,"NoUnderlyings":711,"PosMaintAction":712,"OrigPosReqRefID":713,"PosMaintRptRefID":714,"ClearingBusinessDate":715,"SettlSessID":716,"SettlSessSubID":717,"AdjustmentType":718,"ContraryInstructionIndicator":719,"PriorSpreadIndicator":720,"PosMaintRptID":721,"PosMaintStatus":722,"PosMaintResult":723,"PosReqType":724,"ResponseTransportType":725,"ResponseDestination":726,"TotalNumPosReports":727,"PosReqResult":728,"PosReqStatus":729,"SettlPrice":730,"SettlPriceType":731,"UnderlyingSettlPrice":732,"UnderlyingSettlPriceType":733,"PriorSettlPrice":734,"NoQuoteQualifiers":735,"AllocSettlCurrency":736,"AllocSettlCurrAmt":737,"InterestAtMaturity":738,"LegDatedDate":739,"LegPool":740,"AllocInterestAtMaturity":741,"AllocAccruedInterestAmt":742,"DeliveryDate":743,"AssignmentMethod":744,"AssignmentUnit":745,"OpenInterest":746,"ExerciseMethod":747,"TotNumTradeReports":748,"TradeRequestResult":749,"TradeRequestStatus":750,"TradeReportRejectReason":751,"SideMultiLegReportingType":752,"NoPosAmt":753,"AutoAcceptIndicator":754,"AllocReportID":755,"NoNested2PartyIDs":756,"Nested2PartyID":757,"Nested2PartyIDSource":758,"Nested2PartyRole":759,"Nested2PartySubID":760,"BenchmarkSecurityIDSource":761,"SecuritySubType":762,"UnderlyingSecuritySubType":763,"LegSecuritySubType":764,"AllowableOneSidednessPct":765,"AllowableOneSidednessValue":766,"AllowableOneSidednessCurr":767,"NoTrdRegTimestamps":768,"TrdRegTimestamp":769,"TrdRegTimestampType":770,"TrdRegTimestampOrigin":771,"ConfirmRefID":772,"ConfirmType":773,"ConfirmRejReason":774,"BookingType":775,"IndividualAllocRejCode":776,"SettlInstMsgID":777,"NoSettlInst":778,"LastUpdateTime":779,"AllocSettlInstType":780,"NoSettlPartyIDs":781,"SettlPartyID":782,"SettlPartyIDSource":783,"SettlPartyRole":784,"SettlPartySubID":785,"SettlPartySubIDType":786,"DlvyInstType":787,"TerminationType":788,"NextExpectedMsgSeqNum":789,"OrdStatusReqID":790,"SettlInstReqID":791,"SettlInstReqRejCode":792,"SecondaryAllocID":793,"AllocReportType":794,"AllocReportRefID":795,"AllocCancReplaceReason":796,"CopyMsgIndicator":797,"AllocAccountType":798,"OrderAvgPx":799,"OrderBookingQty":800,"NoSettlPartySubIDs":801,"NoPartySubIDs":802,"PartySubIDType":803,"NoNestedPartySubIDs":804,"NestedPartySubIDType":805,"NoNested2PartySubIDs":806,"Nested2PartySubIDType":807,"AllocIntermedReqType":808,"UnderlyingPx":810,"PriceDelta":811,"ApplQueueMax":812,"ApplQueueDepth":813,"ApplQueueResolution":814,"ApplQueueAction":815,"NoAltMDSource":816,"AltMDSourceID":817,"SecondaryTradeReportID":818,"AvgPxIndicator":819,"TradeLinkID":820,"OrderInputDevice":821,"UnderlyingTradingSessionID":822,"UnderlyingTradingSessionSubID":823,"TradeLegRefID":824,"ExchangeRule":825,"TradeAllocIndicator":826,"ExpirationCycle":827,"TrdType":828,"TrdSubType":829,"TransferReason":830,"TotNumAssignmentReports":832,"AsgnRptID":833,"ThresholdAmount":834,"PegMoveType":835,"PegOffsetType":836,"PegLimitType":837,"PegRoundDirection":838,"PeggedPrice":839,"PegScope":840,"DiscretionMoveType":841,"DiscretionOffsetType":842,"DiscretionLimitType":843,"DiscretionRoundDirection":844,"DiscretionPrice":845,"DiscretionScope":846,"TargetStrategy":847,"TargetStrategyParameters":848,"ParticipationRate":849,"TargetStrategyPerformance":850,"LastLiquidityInd":851,"PublishTrdIndicator":852,"ShortSaleReason":853,"QtyType":854,"SecondaryTrdType":855,"TradeReportType":856,"AllocNoOrdersType":857,"SharedCommission":858,"ConfirmReqID":859,"AvgParPx":860,"ReportedPx":861,"NoCapacities":862,"OrderCapacityQty":863,"NoEvents":864,"EventType":865,"EventDate":866,"EventPx":867,"EventText":868,"PctAtRisk":869,"NoInstrAttrib":870,"InstrAttribType":871,"InstrAttribValue":872,"DatedDate":873,"InterestAccrualDate":874,"CPProgram":875,"CPRegType":876,"UnderlyingCPProgram":877,"UnderlyingCPRegType":878,"UnderlyingQty":879,"TrdMatchID":880,"SecondaryTradeReportRefID":881,"UnderlyingDirtyPrice":882,"UnderlyingEndPrice":883,"UnderlyingStartValue":884,"UnderlyingCurrentValue":885,"UnderlyingEndValue":886,"NoUnderlyingStips":887,"UnderlyingStipType":888,"UnderlyingStipValue":889,"MaturityNetMoney":890,"MiscFeeBasis":891,"TotNoAllocs":892,"LastFragment":893,"CollReqID":894,"CollAsgnReason":895,"CollInquiryQualifier":896,"NoTrades":897,"MarginRatio":898,"MarginExcess":899,"TotalNetValue":900,"CashOutstanding":901,"CollAsgnID":902,"CollAsgnTransType":903,"CollRespID":904,"CollAsgnRespType":905,"CollAsgnRejectReason":906,"CollAsgnRefID":907,"CollRptID":908,"CollInquiryID":909,"CollStatus":910,"TotNumReports":911,"LastRptRequested":912,"AgreementDesc":913,"AgreementID":914,"AgreementDate":915,"StartDate":916,"EndDate":917,"AgreementCurrency":918,"DeliveryType":919,"EndAccruedInterestAmt":920,"StartCash":921,"EndCash":922,"UserRequestID":923,"UserRequestType":924,"NewPassword":925,"UserStatus":926,"UserStatusText":927,"StatusValue":928,"StatusText":929,"RefCompID":930,"RefSubID":931,"NetworkResponseID":932,"NetworkRequestID":933,"LastNetworkResponseID":934,"NetworkRequestType":935,"NoCompIDs":936,"NetworkStatusResponseType":937,"NoCollInquiryQualifier":938,"TrdRptStatus":939,"AffirmStatus":940,"UnderlyingStrikeCurrency":941,"LegStrikeCurrency":942,"TimeBracket":943,"CollAction":944,"CollInquiryStatus":945,"CollInquiryResult":946,"StrikeCurrency":947,"NoNested3PartyIDs":948,"Nested3PartyID":949,"Nested3PartyIDSource":950,"Nested3PartyRole":951,"NoNested3PartySubIDs":952,"Nested3PartySubID":953,"Nested3PartySubIDType":954,"LegContractSettlMonth":955,"LegInterestAccrualDate":956}

class Component:
	def __init__(self):
		self.tag_vals = []

class CommissionData(Component):
	def __init__(self, Commission=None,CommType=None,CommCurrency=None,FundRenewWaiv=None):
		self.tag_vals = []
		if Commission != None:
			self.tag_vals.append((12,Commission))
		if CommType != None:
			self.tag_vals.append((13,CommType))
		if CommCurrency != None:
			self.tag_vals.append((479,CommCurrency))
		if FundRenewWaiv != None:
			self.tag_vals.append((497,FundRenewWaiv))

class DiscretionInstructions(Component):
	def __init__(self, DiscretionInst=None,DiscretionOffsetValue=None,DiscretionMoveType=None,DiscretionOffsetType=None,DiscretionLimitType=None,DiscretionRoundDirection=None,DiscretionScope=None):
		self.tag_vals = []
		if DiscretionInst != None:
			self.tag_vals.append((388,DiscretionInst))
		if DiscretionOffsetValue != None:
			self.tag_vals.append((389,DiscretionOffsetValue))
		if DiscretionMoveType != None:
			self.tag_vals.append((841,DiscretionMoveType))
		if DiscretionOffsetType != None:
			self.tag_vals.append((842,DiscretionOffsetType))
		if DiscretionLimitType != None:
			self.tag_vals.append((843,DiscretionLimitType))
		if DiscretionRoundDirection != None:
			self.tag_vals.append((844,DiscretionRoundDirection))
		if DiscretionScope != None:
			self.tag_vals.append((846,DiscretionScope))

class FinancingDetails(Component):
	def __init__(self, AgreementDesc=None,AgreementID=None,AgreementDate=None,AgreementCurrency=None,TerminationType=None,StartDate=None,EndDate=None,DeliveryType=None,MarginRatio=None):
		self.tag_vals = []
		if AgreementDesc != None:
			self.tag_vals.append((913,AgreementDesc))
		if AgreementID != None:
			self.tag_vals.append((914,AgreementID))
		if AgreementDate != None:
			self.tag_vals.append((915,AgreementDate))
		if AgreementCurrency != None:
			self.tag_vals.append((918,AgreementCurrency))
		if TerminationType != None:
			self.tag_vals.append((788,TerminationType))
		if StartDate != None:
			self.tag_vals.append((916,StartDate))
		if EndDate != None:
			self.tag_vals.append((917,EndDate))
		if DeliveryType != None:
			self.tag_vals.append((919,DeliveryType))
		if MarginRatio != None:
			self.tag_vals.append((898,MarginRatio))

class Instrument(Component):
	def __init__(self, Symbol=None,SymbolSfx=None,SecurityID=None,SecurityIDSource=None,Product=None,CFICode=None,SecurityType=None,SecuritySubType=None,MaturityMonthYear=None,MaturityDate=None,PutOrCall=None,CouponPaymentDate=None,IssueDate=None,RepoCollateralSecurityType=None,RepurchaseTerm=None,RepurchaseRate=None,Factor=None,CreditRating=None,InstrRegistry=None,CountryOfIssue=None,StateOrProvinceOfIssue=None,LocaleOfIssue=None,RedemptionDate=None,StrikePrice=None,StrikeCurrency=None,OptAttribute=None,ContractMultiplier=None,CouponRate=None,SecurityExchange=None,Issuer=None,EncodedIssuerLen=None,EncodedIssuer=None,SecurityDesc=None,EncodedSecurityDescLen=None,EncodedSecurityDesc=None,Pool=None,ContractSettlMonth=None,CPProgram=None,CPRegType=None,DatedDate=None,InterestAccrualDate=None,SecAltIDGrp=None,EvntGrp=None):
		self.tag_vals = []
		if Symbol != None:
			self.tag_vals.append((55,Symbol))
		if SymbolSfx != None:
			self.tag_vals.append((65,SymbolSfx))
		if SecurityID != None:
			self.tag_vals.append((48,SecurityID))
		if SecurityIDSource != None:
			self.tag_vals.append((22,SecurityIDSource))
		if Product != None:
			self.tag_vals.append((460,Product))
		if CFICode != None:
			self.tag_vals.append((461,CFICode))
		if SecurityType != None:
			self.tag_vals.append((167,SecurityType))
		if SecuritySubType != None:
			self.tag_vals.append((762,SecuritySubType))
		if MaturityMonthYear != None:
			self.tag_vals.append((200,MaturityMonthYear))
		if MaturityDate != None:
			self.tag_vals.append((541,MaturityDate))
		if PutOrCall != None:
			self.tag_vals.append((201,PutOrCall))
		if CouponPaymentDate != None:
			self.tag_vals.append((224,CouponPaymentDate))
		if IssueDate != None:
			self.tag_vals.append((225,IssueDate))
		if RepoCollateralSecurityType != None:
			self.tag_vals.append((239,RepoCollateralSecurityType))
		if RepurchaseTerm != None:
			self.tag_vals.append((226,RepurchaseTerm))
		if RepurchaseRate != None:
			self.tag_vals.append((227,RepurchaseRate))
		if Factor != None:
			self.tag_vals.append((228,Factor))
		if CreditRating != None:
			self.tag_vals.append((255,CreditRating))
		if InstrRegistry != None:
			self.tag_vals.append((543,InstrRegistry))
		if CountryOfIssue != None:
			self.tag_vals.append((470,CountryOfIssue))
		if StateOrProvinceOfIssue != None:
			self.tag_vals.append((471,StateOrProvinceOfIssue))
		if LocaleOfIssue != None:
			self.tag_vals.append((472,LocaleOfIssue))
		if RedemptionDate != None:
			self.tag_vals.append((240,RedemptionDate))
		if StrikePrice != None:
			self.tag_vals.append((202,StrikePrice))
		if StrikeCurrency != None:
			self.tag_vals.append((947,StrikeCurrency))
		if OptAttribute != None:
			self.tag_vals.append((206,OptAttribute))
		if ContractMultiplier != None:
			self.tag_vals.append((231,ContractMultiplier))
		if CouponRate != None:
			self.tag_vals.append((223,CouponRate))
		if SecurityExchange != None:
			self.tag_vals.append((207,SecurityExchange))
		if Issuer != None:
			self.tag_vals.append((106,Issuer))
		if EncodedIssuerLen != None:
			self.tag_vals.append((348,EncodedIssuerLen))
		if EncodedIssuer != None:
			self.tag_vals.append((349,EncodedIssuer))
		if SecurityDesc != None:
			self.tag_vals.append((107,SecurityDesc))
		if EncodedSecurityDescLen != None:
			self.tag_vals.append((350,EncodedSecurityDescLen))
		if EncodedSecurityDesc != None:
			self.tag_vals.append((351,EncodedSecurityDesc))
		if Pool != None:
			self.tag_vals.append((691,Pool))
		if ContractSettlMonth != None:
			self.tag_vals.append((667,ContractSettlMonth))
		if CPProgram != None:
			self.tag_vals.append((875,CPProgram))
		if CPRegType != None:
			self.tag_vals.append((876,CPRegType))
		if DatedDate != None:
			self.tag_vals.append((873,DatedDate))
		if InterestAccrualDate != None:
			self.tag_vals.append((874,InterestAccrualDate))
		if SecAltIDGrp != None:
			self.tag_vals+=SecAltIDGrp.tag_vals
		if EvntGrp != None:
			self.tag_vals+=EvntGrp.tag_vals

class InstrumentExtension(Component):
	def __init__(self, DeliveryForm=None,PctAtRisk=None,AttrbGrp=None):
		self.tag_vals = []
		if DeliveryForm != None:
			self.tag_vals.append((668,DeliveryForm))
		if PctAtRisk != None:
			self.tag_vals.append((869,PctAtRisk))
		if AttrbGrp != None:
			self.tag_vals+=AttrbGrp.tag_vals

class InstrumentLeg(Component):
	def __init__(self, LegSymbol=None,LegSymbolSfx=None,LegSecurityID=None,LegSecurityIDSource=None,LegProduct=None,LegCFICode=None,LegSecurityType=None,LegSecuritySubType=None,LegMaturityMonthYear=None,LegMaturityDate=None,LegCouponPaymentDate=None,LegIssueDate=None,LegRepoCollateralSecurityType=None,LegRepurchaseTerm=None,LegRepurchaseRate=None,LegFactor=None,LegCreditRating=None,LegInstrRegistry=None,LegCountryOfIssue=None,LegStateOrProvinceOfIssue=None,LegLocaleOfIssue=None,LegRedemptionDate=None,LegStrikePrice=None,LegStrikeCurrency=None,LegOptAttribute=None,LegContractMultiplier=None,LegCouponRate=None,LegSecurityExchange=None,LegIssuer=None,EncodedLegIssuerLen=None,EncodedLegIssuer=None,LegSecurityDesc=None,EncodedLegSecurityDescLen=None,EncodedLegSecurityDesc=None,LegRatioQty=None,LegSide=None,LegCurrency=None,LegPool=None,LegDatedDate=None,LegContractSettlMonth=None,LegInterestAccrualDate=None,LegSecAltIDGrp=None):
		self.tag_vals = []
		if LegSymbol != None:
			self.tag_vals.append((600,LegSymbol))
		if LegSymbolSfx != None:
			self.tag_vals.append((601,LegSymbolSfx))
		if LegSecurityID != None:
			self.tag_vals.append((602,LegSecurityID))
		if LegSecurityIDSource != None:
			self.tag_vals.append((603,LegSecurityIDSource))
		if LegProduct != None:
			self.tag_vals.append((607,LegProduct))
		if LegCFICode != None:
			self.tag_vals.append((608,LegCFICode))
		if LegSecurityType != None:
			self.tag_vals.append((609,LegSecurityType))
		if LegSecuritySubType != None:
			self.tag_vals.append((764,LegSecuritySubType))
		if LegMaturityMonthYear != None:
			self.tag_vals.append((610,LegMaturityMonthYear))
		if LegMaturityDate != None:
			self.tag_vals.append((611,LegMaturityDate))
		if LegCouponPaymentDate != None:
			self.tag_vals.append((248,LegCouponPaymentDate))
		if LegIssueDate != None:
			self.tag_vals.append((249,LegIssueDate))
		if LegRepoCollateralSecurityType != None:
			self.tag_vals.append((250,LegRepoCollateralSecurityType))
		if LegRepurchaseTerm != None:
			self.tag_vals.append((251,LegRepurchaseTerm))
		if LegRepurchaseRate != None:
			self.tag_vals.append((252,LegRepurchaseRate))
		if LegFactor != None:
			self.tag_vals.append((253,LegFactor))
		if LegCreditRating != None:
			self.tag_vals.append((257,LegCreditRating))
		if LegInstrRegistry != None:
			self.tag_vals.append((599,LegInstrRegistry))
		if LegCountryOfIssue != None:
			self.tag_vals.append((596,LegCountryOfIssue))
		if LegStateOrProvinceOfIssue != None:
			self.tag_vals.append((597,LegStateOrProvinceOfIssue))
		if LegLocaleOfIssue != None:
			self.tag_vals.append((598,LegLocaleOfIssue))
		if LegRedemptionDate != None:
			self.tag_vals.append((254,LegRedemptionDate))
		if LegStrikePrice != None:
			self.tag_vals.append((612,LegStrikePrice))
		if LegStrikeCurrency != None:
			self.tag_vals.append((942,LegStrikeCurrency))
		if LegOptAttribute != None:
			self.tag_vals.append((613,LegOptAttribute))
		if LegContractMultiplier != None:
			self.tag_vals.append((614,LegContractMultiplier))
		if LegCouponRate != None:
			self.tag_vals.append((615,LegCouponRate))
		if LegSecurityExchange != None:
			self.tag_vals.append((616,LegSecurityExchange))
		if LegIssuer != None:
			self.tag_vals.append((617,LegIssuer))
		if EncodedLegIssuerLen != None:
			self.tag_vals.append((618,EncodedLegIssuerLen))
		if EncodedLegIssuer != None:
			self.tag_vals.append((619,EncodedLegIssuer))
		if LegSecurityDesc != None:
			self.tag_vals.append((620,LegSecurityDesc))
		if EncodedLegSecurityDescLen != None:
			self.tag_vals.append((621,EncodedLegSecurityDescLen))
		if EncodedLegSecurityDesc != None:
			self.tag_vals.append((622,EncodedLegSecurityDesc))
		if LegRatioQty != None:
			self.tag_vals.append((623,LegRatioQty))
		if LegSide != None:
			self.tag_vals.append((624,LegSide))
		if LegCurrency != None:
			self.tag_vals.append((556,LegCurrency))
		if LegPool != None:
			self.tag_vals.append((740,LegPool))
		if LegDatedDate != None:
			self.tag_vals.append((739,LegDatedDate))
		if LegContractSettlMonth != None:
			self.tag_vals.append((955,LegContractSettlMonth))
		if LegInterestAccrualDate != None:
			self.tag_vals.append((956,LegInterestAccrualDate))
		if LegSecAltIDGrp != None:
			self.tag_vals+=LegSecAltIDGrp.tag_vals

class LegBenchmarkCurveData(Component):
	def __init__(self, LegBenchmarkCurveCurrency=None,LegBenchmarkCurveName=None,LegBenchmarkCurvePoint=None,LegBenchmarkPrice=None,LegBenchmarkPriceType=None):
		self.tag_vals = []
		if LegBenchmarkCurveCurrency != None:
			self.tag_vals.append((676,LegBenchmarkCurveCurrency))
		if LegBenchmarkCurveName != None:
			self.tag_vals.append((677,LegBenchmarkCurveName))
		if LegBenchmarkCurvePoint != None:
			self.tag_vals.append((678,LegBenchmarkCurvePoint))
		if LegBenchmarkPrice != None:
			self.tag_vals.append((679,LegBenchmarkPrice))
		if LegBenchmarkPriceType != None:
			self.tag_vals.append((680,LegBenchmarkPriceType))

class LegStipulations(Component):
	def __init__(self, NoLegStipulations=None):
		self.tag_vals = []
		if NoLegStipulations != None:
			self.tag_vals.append((683,len(NoLegStipulations)-1))
			for i in range(1,len(NoLegStipulations)):
				for idx,attr in enumerate(NoLegStipulations[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegStipulations[i][idx])

class NestedParties(Component):
	def __init__(self, NoNestedPartyIDs=None):
		self.tag_vals = []
		if NoNestedPartyIDs != None:
			self.tag_vals.append((539,len(NoNestedPartyIDs)-1))
			for i in range(1,len(NoNestedPartyIDs)):
				for idx,attr in enumerate(NoNestedPartyIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoNestedPartyIDs[i][idx])

class OrderQtyData(Component):
	def __init__(self, OrderQty=None,CashOrderQty=None,OrderPercent=None,RoundingDirection=None,RoundingModulus=None):
		self.tag_vals = []
		if OrderQty != None:
			self.tag_vals.append((38,OrderQty))
		if CashOrderQty != None:
			self.tag_vals.append((152,CashOrderQty))
		if OrderPercent != None:
			self.tag_vals.append((516,OrderPercent))
		if RoundingDirection != None:
			self.tag_vals.append((468,RoundingDirection))
		if RoundingModulus != None:
			self.tag_vals.append((469,RoundingModulus))

class Parties(Component):
	def __init__(self, NoPartyIDs=None):
		self.tag_vals = []
		if NoPartyIDs != None:
			self.tag_vals.append((453,len(NoPartyIDs)-1))
			for i in range(1,len(NoPartyIDs)):
				for idx,attr in enumerate(NoPartyIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoPartyIDs[i][idx])

class PegInstructions(Component):
	def __init__(self, PegOffsetValue=None,PegMoveType=None,PegOffsetType=None,PegLimitType=None,PegRoundDirection=None,PegScope=None):
		self.tag_vals = []
		if PegOffsetValue != None:
			self.tag_vals.append((211,PegOffsetValue))
		if PegMoveType != None:
			self.tag_vals.append((835,PegMoveType))
		if PegOffsetType != None:
			self.tag_vals.append((836,PegOffsetType))
		if PegLimitType != None:
			self.tag_vals.append((837,PegLimitType))
		if PegRoundDirection != None:
			self.tag_vals.append((838,PegRoundDirection))
		if PegScope != None:
			self.tag_vals.append((840,PegScope))

class PositionAmountData(Component):
	def __init__(self, NoPosAmt=None):
		self.tag_vals = []
		if NoPosAmt != None:
			self.tag_vals.append((753,len(NoPosAmt)-1))
			for i in range(1,len(NoPosAmt)):
				for idx,attr in enumerate(NoPosAmt[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoPosAmt[i][idx])

class PositionQty(Component):
	def __init__(self, NoPositions=None):
		self.tag_vals = []
		if NoPositions != None:
			self.tag_vals.append((702,len(NoPositions)-1))
			for i in range(1,len(NoPositions)):
				for idx,attr in enumerate(NoPositions[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoPositions[i][idx])

class SettlInstructionsData(Component):
	def __init__(self, SettlDeliveryType=None,StandInstDbType=None,StandInstDbName=None,StandInstDbID=None,DlvyInstGrp=None):
		self.tag_vals = []
		if SettlDeliveryType != None:
			self.tag_vals.append((172,SettlDeliveryType))
		if StandInstDbType != None:
			self.tag_vals.append((169,StandInstDbType))
		if StandInstDbName != None:
			self.tag_vals.append((170,StandInstDbName))
		if StandInstDbID != None:
			self.tag_vals.append((171,StandInstDbID))
		if DlvyInstGrp != None:
			self.tag_vals+=DlvyInstGrp.tag_vals

class SettlParties(Component):
	def __init__(self, NoSettlPartyIDs=None):
		self.tag_vals = []
		if NoSettlPartyIDs != None:
			self.tag_vals.append((781,len(NoSettlPartyIDs)-1))
			for i in range(1,len(NoSettlPartyIDs)):
				for idx,attr in enumerate(NoSettlPartyIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoSettlPartyIDs[i][idx])

class SpreadOrBenchmarkCurveData(Component):
	def __init__(self, Spread=None,BenchmarkCurveCurrency=None,BenchmarkCurveName=None,BenchmarkCurvePoint=None,BenchmarkPrice=None,BenchmarkPriceType=None,BenchmarkSecurityID=None,BenchmarkSecurityIDSource=None):
		self.tag_vals = []
		if Spread != None:
			self.tag_vals.append((218,Spread))
		if BenchmarkCurveCurrency != None:
			self.tag_vals.append((220,BenchmarkCurveCurrency))
		if BenchmarkCurveName != None:
			self.tag_vals.append((221,BenchmarkCurveName))
		if BenchmarkCurvePoint != None:
			self.tag_vals.append((222,BenchmarkCurvePoint))
		if BenchmarkPrice != None:
			self.tag_vals.append((662,BenchmarkPrice))
		if BenchmarkPriceType != None:
			self.tag_vals.append((663,BenchmarkPriceType))
		if BenchmarkSecurityID != None:
			self.tag_vals.append((699,BenchmarkSecurityID))
		if BenchmarkSecurityIDSource != None:
			self.tag_vals.append((761,BenchmarkSecurityIDSource))

class Stipulations(Component):
	def __init__(self, NoStipulations=None):
		self.tag_vals = []
		if NoStipulations != None:
			self.tag_vals.append((232,len(NoStipulations)-1))
			for i in range(1,len(NoStipulations)):
				for idx,attr in enumerate(NoStipulations[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoStipulations[i][idx])

class TrdRegTimestamps(Component):
	def __init__(self, NoTrdRegTimestamps=None):
		self.tag_vals = []
		if NoTrdRegTimestamps != None:
			self.tag_vals.append((768,len(NoTrdRegTimestamps)-1))
			for i in range(1,len(NoTrdRegTimestamps)):
				for idx,attr in enumerate(NoTrdRegTimestamps[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoTrdRegTimestamps[i][idx])

class UnderlyingInstrument(Component):
	def __init__(self, UnderlyingSymbol=None,UnderlyingSymbolSfx=None,UnderlyingSecurityID=None,UnderlyingSecurityIDSource=None,UnderlyingProduct=None,UnderlyingCFICode=None,UnderlyingSecurityType=None,UnderlyingSecuritySubType=None,UnderlyingMaturityMonthYear=None,UnderlyingMaturityDate=None,UnderlyingPutOrCall=None,UnderlyingCouponPaymentDate=None,UnderlyingIssueDate=None,UnderlyingRepoCollateralSecurityType=None,UnderlyingRepurchaseTerm=None,UnderlyingRepurchaseRate=None,UnderlyingFactor=None,UnderlyingCreditRating=None,UnderlyingInstrRegistry=None,UnderlyingCountryOfIssue=None,UnderlyingStateOrProvinceOfIssue=None,UnderlyingLocaleOfIssue=None,UnderlyingRedemptionDate=None,UnderlyingStrikePrice=None,UnderlyingStrikeCurrency=None,UnderlyingOptAttribute=None,UnderlyingContractMultiplier=None,UnderlyingCouponRate=None,UnderlyingSecurityExchange=None,UnderlyingIssuer=None,EncodedUnderlyingIssuerLen=None,EncodedUnderlyingIssuer=None,UnderlyingSecurityDesc=None,EncodedUnderlyingSecurityDescLen=None,EncodedUnderlyingSecurityDesc=None,UnderlyingCPProgram=None,UnderlyingCPRegType=None,UnderlyingCurrency=None,UnderlyingQty=None,UnderlyingPx=None,UnderlyingDirtyPrice=None,UnderlyingEndPrice=None,UnderlyingStartValue=None,UnderlyingCurrentValue=None,UnderlyingEndValue=None,UndSecAltIDGrp=None,UnderlyingStipulations=None):
		self.tag_vals = []
		if UnderlyingSymbol != None:
			self.tag_vals.append((311,UnderlyingSymbol))
		if UnderlyingSymbolSfx != None:
			self.tag_vals.append((312,UnderlyingSymbolSfx))
		if UnderlyingSecurityID != None:
			self.tag_vals.append((309,UnderlyingSecurityID))
		if UnderlyingSecurityIDSource != None:
			self.tag_vals.append((305,UnderlyingSecurityIDSource))
		if UnderlyingProduct != None:
			self.tag_vals.append((462,UnderlyingProduct))
		if UnderlyingCFICode != None:
			self.tag_vals.append((463,UnderlyingCFICode))
		if UnderlyingSecurityType != None:
			self.tag_vals.append((310,UnderlyingSecurityType))
		if UnderlyingSecuritySubType != None:
			self.tag_vals.append((763,UnderlyingSecuritySubType))
		if UnderlyingMaturityMonthYear != None:
			self.tag_vals.append((313,UnderlyingMaturityMonthYear))
		if UnderlyingMaturityDate != None:
			self.tag_vals.append((542,UnderlyingMaturityDate))
		if UnderlyingPutOrCall != None:
			self.tag_vals.append((315,UnderlyingPutOrCall))
		if UnderlyingCouponPaymentDate != None:
			self.tag_vals.append((241,UnderlyingCouponPaymentDate))
		if UnderlyingIssueDate != None:
			self.tag_vals.append((242,UnderlyingIssueDate))
		if UnderlyingRepoCollateralSecurityType != None:
			self.tag_vals.append((243,UnderlyingRepoCollateralSecurityType))
		if UnderlyingRepurchaseTerm != None:
			self.tag_vals.append((244,UnderlyingRepurchaseTerm))
		if UnderlyingRepurchaseRate != None:
			self.tag_vals.append((245,UnderlyingRepurchaseRate))
		if UnderlyingFactor != None:
			self.tag_vals.append((246,UnderlyingFactor))
		if UnderlyingCreditRating != None:
			self.tag_vals.append((256,UnderlyingCreditRating))
		if UnderlyingInstrRegistry != None:
			self.tag_vals.append((595,UnderlyingInstrRegistry))
		if UnderlyingCountryOfIssue != None:
			self.tag_vals.append((592,UnderlyingCountryOfIssue))
		if UnderlyingStateOrProvinceOfIssue != None:
			self.tag_vals.append((593,UnderlyingStateOrProvinceOfIssue))
		if UnderlyingLocaleOfIssue != None:
			self.tag_vals.append((594,UnderlyingLocaleOfIssue))
		if UnderlyingRedemptionDate != None:
			self.tag_vals.append((247,UnderlyingRedemptionDate))
		if UnderlyingStrikePrice != None:
			self.tag_vals.append((316,UnderlyingStrikePrice))
		if UnderlyingStrikeCurrency != None:
			self.tag_vals.append((941,UnderlyingStrikeCurrency))
		if UnderlyingOptAttribute != None:
			self.tag_vals.append((317,UnderlyingOptAttribute))
		if UnderlyingContractMultiplier != None:
			self.tag_vals.append((436,UnderlyingContractMultiplier))
		if UnderlyingCouponRate != None:
			self.tag_vals.append((435,UnderlyingCouponRate))
		if UnderlyingSecurityExchange != None:
			self.tag_vals.append((308,UnderlyingSecurityExchange))
		if UnderlyingIssuer != None:
			self.tag_vals.append((306,UnderlyingIssuer))
		if EncodedUnderlyingIssuerLen != None:
			self.tag_vals.append((362,EncodedUnderlyingIssuerLen))
		if EncodedUnderlyingIssuer != None:
			self.tag_vals.append((363,EncodedUnderlyingIssuer))
		if UnderlyingSecurityDesc != None:
			self.tag_vals.append((307,UnderlyingSecurityDesc))
		if EncodedUnderlyingSecurityDescLen != None:
			self.tag_vals.append((364,EncodedUnderlyingSecurityDescLen))
		if EncodedUnderlyingSecurityDesc != None:
			self.tag_vals.append((365,EncodedUnderlyingSecurityDesc))
		if UnderlyingCPProgram != None:
			self.tag_vals.append((877,UnderlyingCPProgram))
		if UnderlyingCPRegType != None:
			self.tag_vals.append((878,UnderlyingCPRegType))
		if UnderlyingCurrency != None:
			self.tag_vals.append((318,UnderlyingCurrency))
		if UnderlyingQty != None:
			self.tag_vals.append((879,UnderlyingQty))
		if UnderlyingPx != None:
			self.tag_vals.append((810,UnderlyingPx))
		if UnderlyingDirtyPrice != None:
			self.tag_vals.append((882,UnderlyingDirtyPrice))
		if UnderlyingEndPrice != None:
			self.tag_vals.append((883,UnderlyingEndPrice))
		if UnderlyingStartValue != None:
			self.tag_vals.append((884,UnderlyingStartValue))
		if UnderlyingCurrentValue != None:
			self.tag_vals.append((885,UnderlyingCurrentValue))
		if UnderlyingEndValue != None:
			self.tag_vals.append((886,UnderlyingEndValue))
		if UndSecAltIDGrp != None:
			self.tag_vals+=UndSecAltIDGrp.tag_vals
		if UnderlyingStipulations != None:
			self.tag_vals+=UnderlyingStipulations.tag_vals

class YieldData(Component):
	def __init__(self, YieldType=None,Yield=None,YieldCalcDate=None,YieldRedemptionDate=None,YieldRedemptionPrice=None,YieldRedemptionPriceType=None):
		self.tag_vals = []
		if YieldType != None:
			self.tag_vals.append((235,YieldType))
		if Yield != None:
			self.tag_vals.append((236,Yield))
		if YieldCalcDate != None:
			self.tag_vals.append((701,YieldCalcDate))
		if YieldRedemptionDate != None:
			self.tag_vals.append((696,YieldRedemptionDate))
		if YieldRedemptionPrice != None:
			self.tag_vals.append((697,YieldRedemptionPrice))
		if YieldRedemptionPriceType != None:
			self.tag_vals.append((698,YieldRedemptionPriceType))

class UnderlyingStipulations(Component):
	def __init__(self, NoUnderlyingStips=None):
		self.tag_vals = []
		if NoUnderlyingStips != None:
			self.tag_vals.append((887,len(NoUnderlyingStips)-1))
			for i in range(1,len(NoUnderlyingStips)):
				for idx,attr in enumerate(NoUnderlyingStips[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoUnderlyingStips[i][idx])

class NestedParties2(Component):
	def __init__(self, NoNested2PartyIDs=None):
		self.tag_vals = []
		if NoNested2PartyIDs != None:
			self.tag_vals.append((756,len(NoNested2PartyIDs)-1))
			for i in range(1,len(NoNested2PartyIDs)):
				for idx,attr in enumerate(NoNested2PartyIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoNested2PartyIDs[i][idx])

class NestedParties3(Component):
	def __init__(self, NoNested3PartyIDs=None):
		self.tag_vals = []
		if NoNested3PartyIDs != None:
			self.tag_vals.append((948,len(NoNested3PartyIDs)-1))
			for i in range(1,len(NoNested3PartyIDs)):
				for idx,attr in enumerate(NoNested3PartyIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoNested3PartyIDs[i][idx])

class AffectedOrdGrp(Component):
	def __init__(self, NoAffectedOrders=None):
		self.tag_vals = []
		if NoAffectedOrders != None:
			self.tag_vals.append((534,len(NoAffectedOrders)-1))
			for i in range(1,len(NoAffectedOrders)):
				for idx,attr in enumerate(NoAffectedOrders[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoAffectedOrders[i][idx])

class AllocAckGrp(Component):
	def __init__(self, NoAllocs=None):
		self.tag_vals = []
		if NoAllocs != None:
			self.tag_vals.append((78,len(NoAllocs)-1))
			for i in range(1,len(NoAllocs)):
				for idx,attr in enumerate(NoAllocs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoAllocs[i][idx])

class AllocGrp(Component):
	def __init__(self, NoAllocs=None):
		self.tag_vals = []
		if NoAllocs != None:
			self.tag_vals.append((78,len(NoAllocs)-1))
			for i in range(1,len(NoAllocs)):
				for idx,attr in enumerate(NoAllocs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoAllocs[i][idx])

class BidCompReqGrp(Component):
	def __init__(self, NoBidComponents=None):
		self.tag_vals = []
		if NoBidComponents != None:
			self.tag_vals.append((420,len(NoBidComponents)-1))
			for i in range(1,len(NoBidComponents)):
				for idx,attr in enumerate(NoBidComponents[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoBidComponents[i][idx])

class BidCompRspGrp(Component):
	def __init__(self, NoBidComponents):
		self.tag_vals = []
		self.tag_vals.append((420,len(NoBidComponents)-1))
		for i in range(1,len(NoBidComponents)):
			for idx,attr in enumerate(NoBidComponents[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoBidComponents[i][idx])

class BidDescReqGrp(Component):
	def __init__(self, NoBidDescriptors=None):
		self.tag_vals = []
		if NoBidDescriptors != None:
			self.tag_vals.append((398,len(NoBidDescriptors)-1))
			for i in range(1,len(NoBidDescriptors)):
				for idx,attr in enumerate(NoBidDescriptors[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoBidDescriptors[i][idx])

class ClrInstGrp(Component):
	def __init__(self, NoClearingInstructions=None):
		self.tag_vals = []
		if NoClearingInstructions != None:
			self.tag_vals.append((576,len(NoClearingInstructions)-1))
			for i in range(1,len(NoClearingInstructions)):
				for idx,attr in enumerate(NoClearingInstructions[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoClearingInstructions[i][idx])

class CollInqQualGrp(Component):
	def __init__(self, NoCollInquiryQualifier=None):
		self.tag_vals = []
		if NoCollInquiryQualifier != None:
			self.tag_vals.append((938,len(NoCollInquiryQualifier)-1))
			for i in range(1,len(NoCollInquiryQualifier)):
				for idx,attr in enumerate(NoCollInquiryQualifier[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoCollInquiryQualifier[i][idx])

class CompIDReqGrp(Component):
	def __init__(self, NoCompIDs=None):
		self.tag_vals = []
		if NoCompIDs != None:
			self.tag_vals.append((936,len(NoCompIDs)-1))
			for i in range(1,len(NoCompIDs)):
				for idx,attr in enumerate(NoCompIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoCompIDs[i][idx])

class CompIDStatGrp(Component):
	def __init__(self, NoCompIDs):
		self.tag_vals = []
		self.tag_vals.append((936,len(NoCompIDs)-1))
		for i in range(1,len(NoCompIDs)):
			for idx,attr in enumerate(NoCompIDs[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoCompIDs[i][idx])

class ContAmtGrp(Component):
	def __init__(self, NoContAmts=None):
		self.tag_vals = []
		if NoContAmts != None:
			self.tag_vals.append((518,len(NoContAmts)-1))
			for i in range(1,len(NoContAmts)):
				for idx,attr in enumerate(NoContAmts[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoContAmts[i][idx])

class ContraGrp(Component):
	def __init__(self, NoContraBrokers=None):
		self.tag_vals = []
		if NoContraBrokers != None:
			self.tag_vals.append((382,len(NoContraBrokers)-1))
			for i in range(1,len(NoContraBrokers)):
				for idx,attr in enumerate(NoContraBrokers[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoContraBrokers[i][idx])

class CpctyConfGrp(Component):
	def __init__(self, NoCapacities):
		self.tag_vals = []
		self.tag_vals.append((862,len(NoCapacities)-1))
		for i in range(1,len(NoCapacities)):
			for idx,attr in enumerate(NoCapacities[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoCapacities[i][idx])

class ExecAllocGrp(Component):
	def __init__(self, NoExecs=None):
		self.tag_vals = []
		if NoExecs != None:
			self.tag_vals.append((124,len(NoExecs)-1))
			for i in range(1,len(NoExecs)):
				for idx,attr in enumerate(NoExecs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoExecs[i][idx])

class ExecCollGrp(Component):
	def __init__(self, NoExecs=None):
		self.tag_vals = []
		if NoExecs != None:
			self.tag_vals.append((124,len(NoExecs)-1))
			for i in range(1,len(NoExecs)):
				for idx,attr in enumerate(NoExecs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoExecs[i][idx])

class ExecsGrp(Component):
	def __init__(self, NoExecs=None):
		self.tag_vals = []
		if NoExecs != None:
			self.tag_vals.append((124,len(NoExecs)-1))
			for i in range(1,len(NoExecs)):
				for idx,attr in enumerate(NoExecs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoExecs[i][idx])

class InstrmtGrp(Component):
	def __init__(self, NoRelatedSym=None):
		self.tag_vals = []
		if NoRelatedSym != None:
			self.tag_vals.append((146,len(NoRelatedSym)-1))
			for i in range(1,len(NoRelatedSym)):
				for idx,attr in enumerate(NoRelatedSym[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoRelatedSym[i][idx])

class InstrmtLegExecGrp(Component):
	def __init__(self, NoLegs=None):
		self.tag_vals = []
		if NoLegs != None:
			self.tag_vals.append((555,len(NoLegs)-1))
			for i in range(1,len(NoLegs)):
				for idx,attr in enumerate(NoLegs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegs[i][idx])

class InstrmtLegGrp(Component):
	def __init__(self, NoLegs=None):
		self.tag_vals = []
		if NoLegs != None:
			self.tag_vals.append((555,len(NoLegs)-1))
			for i in range(1,len(NoLegs)):
				for idx,attr in enumerate(NoLegs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegs[i][idx])

class InstrmtLegIOIGrp(Component):
	def __init__(self, NoLegs=None):
		self.tag_vals = []
		if NoLegs != None:
			self.tag_vals.append((555,len(NoLegs)-1))
			for i in range(1,len(NoLegs)):
				for idx,attr in enumerate(NoLegs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegs[i][idx])

class InstrmtLegSecListGrp(Component):
	def __init__(self, NoLegs=None):
		self.tag_vals = []
		if NoLegs != None:
			self.tag_vals.append((555,len(NoLegs)-1))
			for i in range(1,len(NoLegs)):
				for idx,attr in enumerate(NoLegs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegs[i][idx])

class InstrmtMDReqGrp(Component):
	def __init__(self, NoRelatedSym):
		self.tag_vals = []
		self.tag_vals.append((146,len(NoRelatedSym)-1))
		for i in range(1,len(NoRelatedSym)):
			for idx,attr in enumerate(NoRelatedSym[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoRelatedSym[i][idx])

class InstrmtStrkPxGrp(Component):
	def __init__(self, NoStrikes):
		self.tag_vals = []
		self.tag_vals.append((428,len(NoStrikes)-1))
		for i in range(1,len(NoStrikes)):
			for idx,attr in enumerate(NoStrikes[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoStrikes[i][idx])

class IOIQualGrp(Component):
	def __init__(self, NoIOIQualifiers=None):
		self.tag_vals = []
		if NoIOIQualifiers != None:
			self.tag_vals.append((199,len(NoIOIQualifiers)-1))
			for i in range(1,len(NoIOIQualifiers)):
				for idx,attr in enumerate(NoIOIQualifiers[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoIOIQualifiers[i][idx])

class LegOrdGrp(Component):
	def __init__(self, NoLegs):
		self.tag_vals = []
		self.tag_vals.append((555,len(NoLegs)-1))
		for i in range(1,len(NoLegs)):
			for idx,attr in enumerate(NoLegs[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoLegs[i][idx])

class LegPreAllocGrp(Component):
	def __init__(self, NoLegAllocs=None):
		self.tag_vals = []
		if NoLegAllocs != None:
			self.tag_vals.append((670,len(NoLegAllocs)-1))
			for i in range(1,len(NoLegAllocs)):
				for idx,attr in enumerate(NoLegAllocs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegAllocs[i][idx])

class LegQuotGrp(Component):
	def __init__(self, NoLegs=None):
		self.tag_vals = []
		if NoLegs != None:
			self.tag_vals.append((555,len(NoLegs)-1))
			for i in range(1,len(NoLegs)):
				for idx,attr in enumerate(NoLegs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegs[i][idx])

class LegQuotStatGrp(Component):
	def __init__(self, NoLegs=None):
		self.tag_vals = []
		if NoLegs != None:
			self.tag_vals.append((555,len(NoLegs)-1))
			for i in range(1,len(NoLegs)):
				for idx,attr in enumerate(NoLegs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegs[i][idx])

class LinesOfTextGrp(Component):
	def __init__(self, NoLinesOfText):
		self.tag_vals = []
		self.tag_vals.append((33,len(NoLinesOfText)-1))
		for i in range(1,len(NoLinesOfText)):
			for idx,attr in enumerate(NoLinesOfText[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoLinesOfText[i][idx])

class ListOrdGrp(Component):
	def __init__(self, NoOrders):
		self.tag_vals = []
		self.tag_vals.append((73,len(NoOrders)-1))
		for i in range(1,len(NoOrders)):
			for idx,attr in enumerate(NoOrders[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoOrders[i][idx])

class MDFullGrp(Component):
	def __init__(self, NoMDEntries):
		self.tag_vals = []
		self.tag_vals.append((268,len(NoMDEntries)-1))
		for i in range(1,len(NoMDEntries)):
			for idx,attr in enumerate(NoMDEntries[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoMDEntries[i][idx])

class MDIncGrp(Component):
	def __init__(self, NoMDEntries):
		self.tag_vals = []
		self.tag_vals.append((268,len(NoMDEntries)-1))
		for i in range(1,len(NoMDEntries)):
			for idx,attr in enumerate(NoMDEntries[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoMDEntries[i][idx])

class MDReqGrp(Component):
	def __init__(self, NoMDEntryTypes):
		self.tag_vals = []
		self.tag_vals.append((267,len(NoMDEntryTypes)-1))
		for i in range(1,len(NoMDEntryTypes)):
			for idx,attr in enumerate(NoMDEntryTypes[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoMDEntryTypes[i][idx])

class MDRjctGrp(Component):
	def __init__(self, NoAltMDSource=None):
		self.tag_vals = []
		if NoAltMDSource != None:
			self.tag_vals.append((816,len(NoAltMDSource)-1))
			for i in range(1,len(NoAltMDSource)):
				for idx,attr in enumerate(NoAltMDSource[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoAltMDSource[i][idx])

class MiscFeesGrp(Component):
	def __init__(self, NoMiscFees=None):
		self.tag_vals = []
		if NoMiscFees != None:
			self.tag_vals.append((136,len(NoMiscFees)-1))
			for i in range(1,len(NoMiscFees)):
				for idx,attr in enumerate(NoMiscFees[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoMiscFees[i][idx])

class OrdAllocGrp(Component):
	def __init__(self, NoOrders=None):
		self.tag_vals = []
		if NoOrders != None:
			self.tag_vals.append((73,len(NoOrders)-1))
			for i in range(1,len(NoOrders)):
				for idx,attr in enumerate(NoOrders[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoOrders[i][idx])

class OrdListStatGrp(Component):
	def __init__(self, NoOrders):
		self.tag_vals = []
		self.tag_vals.append((73,len(NoOrders)-1))
		for i in range(1,len(NoOrders)):
			for idx,attr in enumerate(NoOrders[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoOrders[i][idx])

class PosUndInstrmtGrp(Component):
	def __init__(self, NoUnderlyings=None):
		self.tag_vals = []
		if NoUnderlyings != None:
			self.tag_vals.append((711,len(NoUnderlyings)-1))
			for i in range(1,len(NoUnderlyings)):
				for idx,attr in enumerate(NoUnderlyings[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoUnderlyings[i][idx])

class PreAllocGrp(Component):
	def __init__(self, NoAllocs=None):
		self.tag_vals = []
		if NoAllocs != None:
			self.tag_vals.append((78,len(NoAllocs)-1))
			for i in range(1,len(NoAllocs)):
				for idx,attr in enumerate(NoAllocs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoAllocs[i][idx])

class PreAllocMlegGrp(Component):
	def __init__(self, NoAllocs=None):
		self.tag_vals = []
		if NoAllocs != None:
			self.tag_vals.append((78,len(NoAllocs)-1))
			for i in range(1,len(NoAllocs)):
				for idx,attr in enumerate(NoAllocs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoAllocs[i][idx])

class QuotCxlEntriesGrp(Component):
	def __init__(self, NoQuoteEntries=None):
		self.tag_vals = []
		if NoQuoteEntries != None:
			self.tag_vals.append((295,len(NoQuoteEntries)-1))
			for i in range(1,len(NoQuoteEntries)):
				for idx,attr in enumerate(NoQuoteEntries[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoQuoteEntries[i][idx])

class QuotEntryAckGrp(Component):
	def __init__(self, NoQuoteEntries=None):
		self.tag_vals = []
		if NoQuoteEntries != None:
			self.tag_vals.append((295,len(NoQuoteEntries)-1))
			for i in range(1,len(NoQuoteEntries)):
				for idx,attr in enumerate(NoQuoteEntries[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoQuoteEntries[i][idx])

class QuotEntryGrp(Component):
	def __init__(self, NoQuoteEntries):
		self.tag_vals = []
		self.tag_vals.append((295,len(NoQuoteEntries)-1))
		for i in range(1,len(NoQuoteEntries)):
			for idx,attr in enumerate(NoQuoteEntries[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoQuoteEntries[i][idx])

class QuotQualGrp(Component):
	def __init__(self, NoQuoteQualifiers=None):
		self.tag_vals = []
		if NoQuoteQualifiers != None:
			self.tag_vals.append((735,len(NoQuoteQualifiers)-1))
			for i in range(1,len(NoQuoteQualifiers)):
				for idx,attr in enumerate(NoQuoteQualifiers[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoQuoteQualifiers[i][idx])

class QuotReqGrp(Component):
	def __init__(self, NoRelatedSym):
		self.tag_vals = []
		self.tag_vals.append((146,len(NoRelatedSym)-1))
		for i in range(1,len(NoRelatedSym)):
			for idx,attr in enumerate(NoRelatedSym[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoRelatedSym[i][idx])

class QuotReqLegsGrp(Component):
	def __init__(self, NoLegs=None):
		self.tag_vals = []
		if NoLegs != None:
			self.tag_vals.append((555,len(NoLegs)-1))
			for i in range(1,len(NoLegs)):
				for idx,attr in enumerate(NoLegs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegs[i][idx])

class QuotReqRjctGrp(Component):
	def __init__(self, NoRelatedSym):
		self.tag_vals = []
		self.tag_vals.append((146,len(NoRelatedSym)-1))
		for i in range(1,len(NoRelatedSym)):
			for idx,attr in enumerate(NoRelatedSym[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoRelatedSym[i][idx])

class QuotSetAckGrp(Component):
	def __init__(self, NoQuoteSets=None):
		self.tag_vals = []
		if NoQuoteSets != None:
			self.tag_vals.append((296,len(NoQuoteSets)-1))
			for i in range(1,len(NoQuoteSets)):
				for idx,attr in enumerate(NoQuoteSets[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoQuoteSets[i][idx])

class QuotSetGrp(Component):
	def __init__(self, NoQuoteSets):
		self.tag_vals = []
		self.tag_vals.append((296,len(NoQuoteSets)-1))
		for i in range(1,len(NoQuoteSets)):
			for idx,attr in enumerate(NoQuoteSets[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoQuoteSets[i][idx])

class RelSymDerivSecGrp(Component):
	def __init__(self, NoRelatedSym=None):
		self.tag_vals = []
		if NoRelatedSym != None:
			self.tag_vals.append((146,len(NoRelatedSym)-1))
			for i in range(1,len(NoRelatedSym)):
				for idx,attr in enumerate(NoRelatedSym[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoRelatedSym[i][idx])

class RFQReqGrp(Component):
	def __init__(self, NoRelatedSym):
		self.tag_vals = []
		self.tag_vals.append((146,len(NoRelatedSym)-1))
		for i in range(1,len(NoRelatedSym)):
			for idx,attr in enumerate(NoRelatedSym[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoRelatedSym[i][idx])

class RgstDistInstGrp(Component):
	def __init__(self, NoDistribInsts=None):
		self.tag_vals = []
		if NoDistribInsts != None:
			self.tag_vals.append((510,len(NoDistribInsts)-1))
			for i in range(1,len(NoDistribInsts)):
				for idx,attr in enumerate(NoDistribInsts[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoDistribInsts[i][idx])

class RgstDtlsGrp(Component):
	def __init__(self, NoRegistDtls=None):
		self.tag_vals = []
		if NoRegistDtls != None:
			self.tag_vals.append((473,len(NoRegistDtls)-1))
			for i in range(1,len(NoRegistDtls)):
				for idx,attr in enumerate(NoRegistDtls[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoRegistDtls[i][idx])

class RoutingGrp(Component):
	def __init__(self, NoRoutingIDs=None):
		self.tag_vals = []
		if NoRoutingIDs != None:
			self.tag_vals.append((215,len(NoRoutingIDs)-1))
			for i in range(1,len(NoRoutingIDs)):
				for idx,attr in enumerate(NoRoutingIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoRoutingIDs[i][idx])

class SecListGrp(Component):
	def __init__(self, NoRelatedSym=None):
		self.tag_vals = []
		if NoRelatedSym != None:
			self.tag_vals.append((146,len(NoRelatedSym)-1))
			for i in range(1,len(NoRelatedSym)):
				for idx,attr in enumerate(NoRelatedSym[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoRelatedSym[i][idx])

class SecTypesGrp(Component):
	def __init__(self, NoSecurityTypes=None):
		self.tag_vals = []
		if NoSecurityTypes != None:
			self.tag_vals.append((558,len(NoSecurityTypes)-1))
			for i in range(1,len(NoSecurityTypes)):
				for idx,attr in enumerate(NoSecurityTypes[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoSecurityTypes[i][idx])

class SettlInstGrp(Component):
	def __init__(self, NoSettlInst=None):
		self.tag_vals = []
		if NoSettlInst != None:
			self.tag_vals.append((778,len(NoSettlInst)-1))
			for i in range(1,len(NoSettlInst)):
				for idx,attr in enumerate(NoSettlInst[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoSettlInst[i][idx])

class SideCrossOrdCxlGrp(Component):
	def __init__(self, NoSides):
		self.tag_vals = []
		self.tag_vals.append((552,len(NoSides)-1))
		for i in range(1,len(NoSides)):
			for idx,attr in enumerate(NoSides[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoSides[i][idx])

class SideCrossOrdModGrp(Component):
	def __init__(self, NoSides):
		self.tag_vals = []
		self.tag_vals.append((552,len(NoSides)-1))
		for i in range(1,len(NoSides)):
			for idx,attr in enumerate(NoSides[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoSides[i][idx])

class TrdAllocGrp(Component):
	def __init__(self, NoAllocs=None):
		self.tag_vals = []
		if NoAllocs != None:
			self.tag_vals.append((78,len(NoAllocs)-1))
			for i in range(1,len(NoAllocs)):
				for idx,attr in enumerate(NoAllocs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoAllocs[i][idx])

class TrdCapRptSideGrp(Component):
	def __init__(self, NoSides):
		self.tag_vals = []
		self.tag_vals.append((552,len(NoSides)-1))
		for i in range(1,len(NoSides)):
			for idx,attr in enumerate(NoSides[0]):
				if attr in components_names:
					self.tag_vals+=attr.tag_vals
				else:
					self.tag_vals.append(tag_name_to_num[attr],NoSides[i][idx])

class TrdCollGrp(Component):
	def __init__(self, NoTrades=None):
		self.tag_vals = []
		if NoTrades != None:
			self.tag_vals.append((897,len(NoTrades)-1))
			for i in range(1,len(NoTrades)):
				for idx,attr in enumerate(NoTrades[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoTrades[i][idx])

class TrdInstrmtLegGrp(Component):
	def __init__(self, NoLegs=None):
		self.tag_vals = []
		if NoLegs != None:
			self.tag_vals.append((555,len(NoLegs)-1))
			for i in range(1,len(NoLegs)):
				for idx,attr in enumerate(NoLegs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegs[i][idx])

class TrdgSesGrp(Component):
	def __init__(self, NoTradingSessions=None):
		self.tag_vals = []
		if NoTradingSessions != None:
			self.tag_vals.append((386,len(NoTradingSessions)-1))
			for i in range(1,len(NoTradingSessions)):
				for idx,attr in enumerate(NoTradingSessions[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoTradingSessions[i][idx])

class UndInstrmtCollGrp(Component):
	def __init__(self, NoUnderlyings=None):
		self.tag_vals = []
		if NoUnderlyings != None:
			self.tag_vals.append((711,len(NoUnderlyings)-1))
			for i in range(1,len(NoUnderlyings)):
				for idx,attr in enumerate(NoUnderlyings[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoUnderlyings[i][idx])

class UndInstrmtGrp(Component):
	def __init__(self, NoUnderlyings=None):
		self.tag_vals = []
		if NoUnderlyings != None:
			self.tag_vals.append((711,len(NoUnderlyings)-1))
			for i in range(1,len(NoUnderlyings)):
				for idx,attr in enumerate(NoUnderlyings[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoUnderlyings[i][idx])

class UndInstrmtStrkPxGrp(Component):
	def __init__(self, NoUnderlyings=None):
		self.tag_vals = []
		if NoUnderlyings != None:
			self.tag_vals.append((711,len(NoUnderlyings)-1))
			for i in range(1,len(NoUnderlyings)):
				for idx,attr in enumerate(NoUnderlyings[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoUnderlyings[i][idx])

class TrdCapDtGrp(Component):
	def __init__(self, NoDates=None):
		self.tag_vals = []
		if NoDates != None:
			self.tag_vals.append((580,len(NoDates)-1))
			for i in range(1,len(NoDates)):
				for idx,attr in enumerate(NoDates[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoDates[i][idx])

class EvntGrp(Component):
	def __init__(self, NoEvents=None):
		self.tag_vals = []
		if NoEvents != None:
			self.tag_vals.append((864,len(NoEvents)-1))
			for i in range(1,len(NoEvents)):
				for idx,attr in enumerate(NoEvents[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoEvents[i][idx])

class SecAltIDGrp(Component):
	def __init__(self, NoSecurityAltID=None):
		self.tag_vals = []
		if NoSecurityAltID != None:
			self.tag_vals.append((454,len(NoSecurityAltID)-1))
			for i in range(1,len(NoSecurityAltID)):
				for idx,attr in enumerate(NoSecurityAltID[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoSecurityAltID[i][idx])

class LegSecAltIDGrp(Component):
	def __init__(self, NoLegSecurityAltID=None):
		self.tag_vals = []
		if NoLegSecurityAltID != None:
			self.tag_vals.append((604,len(NoLegSecurityAltID)-1))
			for i in range(1,len(NoLegSecurityAltID)):
				for idx,attr in enumerate(NoLegSecurityAltID[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoLegSecurityAltID[i][idx])

class UndSecAltIDGrp(Component):
	def __init__(self, NoUnderlyingSecurityAltID=None):
		self.tag_vals = []
		if NoUnderlyingSecurityAltID != None:
			self.tag_vals.append((457,len(NoUnderlyingSecurityAltID)-1))
			for i in range(1,len(NoUnderlyingSecurityAltID)):
				for idx,attr in enumerate(NoUnderlyingSecurityAltID[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoUnderlyingSecurityAltID[i][idx])

class AttrbGrp(Component):
	def __init__(self, NoInstrAttrib=None):
		self.tag_vals = []
		if NoInstrAttrib != None:
			self.tag_vals.append((870,len(NoInstrAttrib)-1))
			for i in range(1,len(NoInstrAttrib)):
				for idx,attr in enumerate(NoInstrAttrib[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoInstrAttrib[i][idx])

class DlvyInstGrp(Component):
	def __init__(self, NoDlvyInst=None):
		self.tag_vals = []
		if NoDlvyInst != None:
			self.tag_vals.append((85,len(NoDlvyInst)-1))
			for i in range(1,len(NoDlvyInst)):
				for idx,attr in enumerate(NoDlvyInst[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoDlvyInst[i][idx])

class SettlPtysSubGrp(Component):
	def __init__(self, NoSettlPartySubIDs=None):
		self.tag_vals = []
		if NoSettlPartySubIDs != None:
			self.tag_vals.append((801,len(NoSettlPartySubIDs)-1))
			for i in range(1,len(NoSettlPartySubIDs)):
				for idx,attr in enumerate(NoSettlPartySubIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoSettlPartySubIDs[i][idx])

class PtysSubGrp(Component):
	def __init__(self, NoPartySubIDs=None):
		self.tag_vals = []
		if NoPartySubIDs != None:
			self.tag_vals.append((802,len(NoPartySubIDs)-1))
			for i in range(1,len(NoPartySubIDs)):
				for idx,attr in enumerate(NoPartySubIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoPartySubIDs[i][idx])

class NstdPtysSubGrp(Component):
	def __init__(self, NoNestedPartySubIDs=None):
		self.tag_vals = []
		if NoNestedPartySubIDs != None:
			self.tag_vals.append((804,len(NoNestedPartySubIDs)-1))
			for i in range(1,len(NoNestedPartySubIDs)):
				for idx,attr in enumerate(NoNestedPartySubIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoNestedPartySubIDs[i][idx])

class NstdPtys2SubGrp(Component):
	def __init__(self, NoNested2PartySubIDs=None):
		self.tag_vals = []
		if NoNested2PartySubIDs != None:
			self.tag_vals.append((806,len(NoNested2PartySubIDs)-1))
			for i in range(1,len(NoNested2PartySubIDs)):
				for idx,attr in enumerate(NoNested2PartySubIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoNested2PartySubIDs[i][idx])

class NstdPtys3SubGrp(Component):
	def __init__(self, NoNested3PartySubIDs=None):
		self.tag_vals = []
		if NoNested3PartySubIDs != None:
			self.tag_vals.append((952,len(NoNested3PartySubIDs)-1))
			for i in range(1,len(NoNested3PartySubIDs)):
				for idx,attr in enumerate(NoNested3PartySubIDs[0]):
					if attr in components_names:
						self.tag_vals+=attr.tag_vals
					else:
						self.tag_vals.append(tag_name_to_num[attr],NoNested3PartySubIDs[i][idx])

def Heartbeat(MsgSeqNum,TargetCompID,TestReqID=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,0,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	if TestReqID != None:
		msg.append_pair(112,TestReqID)
	return msg.encode()

def TestRequest(MsgSeqNum,TargetCompID,TestReqID):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,1,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(112,TestReqID)
	return msg.encode()

def ResendRequest(MsgSeqNum,TargetCompID,BeginSeqNo,EndSeqNo):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,2,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(7,BeginSeqNo)
	msg.append_pair(16,EndSeqNo)
	return msg.encode()

def Reject(MsgSeqNum,TargetCompID,RefSeqNum,RefTagID=None,RefMsgType=None,SessionRejectReason=None,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,3,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(45,RefSeqNum)
	if RefTagID != None:
		msg.append_pair(371,RefTagID)
	if RefMsgType != None:
		msg.append_pair(372,RefMsgType)
	if SessionRejectReason != None:
		msg.append_pair(373,SessionRejectReason)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def SequenceReset(MsgSeqNum,TargetCompID,NewSeqNo,GapFillFlag=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,4,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(36,NewSeqNo)
	if GapFillFlag != None:
		msg.append_pair(123,GapFillFlag)
	return msg.encode()

def Logout(MsgSeqNum,TargetCompID,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,5,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def IOI(MsgSeqNum,TargetCompID,IOIID,IOITransType,Side,IOIQty,Instrument,IOIRefID=None,QtyType=None,Currency=None,PriceType=None,Price=None,ValidUntilTime=None,IOIQltyInd=None,IOINaturalFlag=None,Text=None,EncodedTextLen=None,EncodedText=None,TransactTime=None,URLLink=None,FinancingDetails=None,UndInstrmtGrp=None,OrderQtyData=None,Stipulations=None,InstrmtLegIOIGrp=None,IOIQualGrp=None,RoutingGrp=None,SpreadOrBenchmarkCurveData=None,YieldData=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,6,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(23,IOIID)
	msg.append_pair(28,IOITransType)
	msg.append_pair(54,Side)
	msg.append_pair(27,IOIQty)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if IOIRefID != None:
		msg.append_pair(26,IOIRefID)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if Price != None:
		msg.append_pair(44,Price)
	if ValidUntilTime != None:
		msg.append_pair(62,ValidUntilTime)
	if IOIQltyInd != None:
		msg.append_pair(25,IOIQltyInd)
	if IOINaturalFlag != None:
		msg.append_pair(130,IOINaturalFlag)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if URLLink != None:
		msg.append_pair(149,URLLink)
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if OrderQtyData != None:
		for tv in OrderQtyData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegIOIGrp != None:
		for tv in InstrmtLegIOIGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if IOIQualGrp != None:
		for tv in IOIQualGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if RoutingGrp != None:
		for tv in RoutingGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def Advertisement(MsgSeqNum,TargetCompID,AdvId,AdvTransType,AdvSide,Quantity,Instrument,AdvRefID=None,QtyType=None,Price=None,Currency=None,TradeDate=None,TransactTime=None,Text=None,EncodedTextLen=None,EncodedText=None,URLLink=None,LastMkt=None,TradingSessionID=None,TradingSessionSubID=None,InstrmtLegGrp=None,UndInstrmtGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,7,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(2,AdvId)
	msg.append_pair(5,AdvTransType)
	msg.append_pair(4,AdvSide)
	msg.append_pair(53,Quantity)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if AdvRefID != None:
		msg.append_pair(3,AdvRefID)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if Price != None:
		msg.append_pair(44,Price)
	if Currency != None:
		msg.append_pair(15,Currency)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if URLLink != None:
		msg.append_pair(149,URLLink)
	if LastMkt != None:
		msg.append_pair(30,LastMkt)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def ExecutionReport(MsgSeqNum,TargetCompID,OrderID,ExecID,ExecType,OrdStatus,Side,LeavesQty,CumQty,AvgPx,Instrument,SecondaryOrderID=None,SecondaryClOrdID=None,SecondaryExecID=None,ClOrdID=None,OrigClOrdID=None,ClOrdLinkID=None,QuoteRespID=None,OrdStatusReqID=None,MassStatusReqID=None,TotNumReports=None,LastRptRequested=None,TradeOriginationDate=None,ListID=None,CrossID=None,OrigCrossID=None,CrossType=None,ExecRefID=None,WorkingIndicator=None,OrdRejReason=None,ExecRestatementReason=None,Account=None,AcctIDSource=None,AccountType=None,DayBookingInst=None,BookingUnit=None,PreallocMethod=None,SettlType=None,SettlDate=None,CashMargin=None,ClearingFeeIndicator=None,QtyType=None,OrdType=None,PriceType=None,Price=None,StopPx=None,PeggedPrice=None,DiscretionPrice=None,TargetStrategy=None,TargetStrategyParameters=None,ParticipationRate=None,TargetStrategyPerformance=None,Currency=None,ComplianceID=None,SolicitedFlag=None,TimeInForce=None,EffectiveTime=None,ExpireDate=None,ExpireTime=None,ExecInst=None,OrderCapacity=None,OrderRestrictions=None,CustOrderCapacity=None,LastQty=None,UnderlyingLastQty=None,LastPx=None,UnderlyingLastPx=None,LastParPx=None,LastSpotRate=None,LastForwardPoints=None,LastMkt=None,TradingSessionID=None,TradingSessionSubID=None,TimeBracket=None,LastCapacity=None,DayOrderQty=None,DayCumQty=None,DayAvgPx=None,GTBookingInst=None,TradeDate=None,TransactTime=None,ReportToExch=None,GrossTradeAmt=None,NumDaysInterest=None,ExDate=None,AccruedInterestRate=None,AccruedInterestAmt=None,InterestAtMaturity=None,EndAccruedInterestAmt=None,StartCash=None,EndCash=None,TradedFlatSwitch=None,BasisFeatureDate=None,BasisFeaturePrice=None,Concession=None,TotalTakedown=None,NetMoney=None,SettlCurrAmt=None,SettlCurrency=None,SettlCurrFxRate=None,SettlCurrFxRateCalc=None,HandlInst=None,MinQty=None,MaxFloor=None,PositionEffect=None,MaxShow=None,BookingType=None,Text=None,EncodedTextLen=None,EncodedText=None,SettlDate2=None,OrderQty2=None,LastForwardPoints2=None,MultiLegReportingType=None,CancellationRights=None,MoneyLaunderingStatus=None,RegistID=None,Designation=None,TransBkdTime=None,ExecValuationPoint=None,ExecPriceType=None,ExecPriceAdjustment=None,PriorityIndicator=None,PriceImprovement=None,LastLiquidityInd=None,CopyMsgIndicator=None,Parties=None,ContraGrp=None,FinancingDetails=None,UndInstrmtGrp=None,Stipulations=None,OrderQtyData=None,PegInstructions=None,DiscretionInstructions=None,CommissionData=None,SpreadOrBenchmarkCurveData=None,YieldData=None,ContAmtGrp=None,InstrmtLegExecGrp=None,MiscFeesGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,8,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(37,OrderID)
	msg.append_pair(17,ExecID)
	msg.append_pair(150,ExecType)
	msg.append_pair(39,OrdStatus)
	msg.append_pair(54,Side)
	msg.append_pair(151,LeavesQty)
	msg.append_pair(14,CumQty)
	msg.append_pair(6,AvgPx)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if SecondaryExecID != None:
		msg.append_pair(527,SecondaryExecID)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if OrigClOrdID != None:
		msg.append_pair(41,OrigClOrdID)
	if ClOrdLinkID != None:
		msg.append_pair(583,ClOrdLinkID)
	if QuoteRespID != None:
		msg.append_pair(693,QuoteRespID)
	if OrdStatusReqID != None:
		msg.append_pair(790,OrdStatusReqID)
	if MassStatusReqID != None:
		msg.append_pair(584,MassStatusReqID)
	if TotNumReports != None:
		msg.append_pair(911,TotNumReports)
	if LastRptRequested != None:
		msg.append_pair(912,LastRptRequested)
	if TradeOriginationDate != None:
		msg.append_pair(229,TradeOriginationDate)
	if ListID != None:
		msg.append_pair(66,ListID)
	if CrossID != None:
		msg.append_pair(548,CrossID)
	if OrigCrossID != None:
		msg.append_pair(551,OrigCrossID)
	if CrossType != None:
		msg.append_pair(549,CrossType)
	if ExecRefID != None:
		msg.append_pair(19,ExecRefID)
	if WorkingIndicator != None:
		msg.append_pair(636,WorkingIndicator)
	if OrdRejReason != None:
		msg.append_pair(103,OrdRejReason)
	if ExecRestatementReason != None:
		msg.append_pair(378,ExecRestatementReason)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if DayBookingInst != None:
		msg.append_pair(589,DayBookingInst)
	if BookingUnit != None:
		msg.append_pair(590,BookingUnit)
	if PreallocMethod != None:
		msg.append_pair(591,PreallocMethod)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if CashMargin != None:
		msg.append_pair(544,CashMargin)
	if ClearingFeeIndicator != None:
		msg.append_pair(635,ClearingFeeIndicator)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if OrdType != None:
		msg.append_pair(40,OrdType)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if Price != None:
		msg.append_pair(44,Price)
	if StopPx != None:
		msg.append_pair(99,StopPx)
	if PeggedPrice != None:
		msg.append_pair(839,PeggedPrice)
	if DiscretionPrice != None:
		msg.append_pair(845,DiscretionPrice)
	if TargetStrategy != None:
		msg.append_pair(847,TargetStrategy)
	if TargetStrategyParameters != None:
		msg.append_pair(848,TargetStrategyParameters)
	if ParticipationRate != None:
		msg.append_pair(849,ParticipationRate)
	if TargetStrategyPerformance != None:
		msg.append_pair(850,TargetStrategyPerformance)
	if Currency != None:
		msg.append_pair(15,Currency)
	if ComplianceID != None:
		msg.append_pair(376,ComplianceID)
	if SolicitedFlag != None:
		msg.append_pair(377,SolicitedFlag)
	if TimeInForce != None:
		msg.append_pair(59,TimeInForce)
	if EffectiveTime != None:
		msg.append_pair(168,EffectiveTime)
	if ExpireDate != None:
		msg.append_pair(432,ExpireDate)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if ExecInst != None:
		msg.append_pair(18,ExecInst)
	if OrderCapacity != None:
		msg.append_pair(528,OrderCapacity)
	if OrderRestrictions != None:
		msg.append_pair(529,OrderRestrictions)
	if CustOrderCapacity != None:
		msg.append_pair(582,CustOrderCapacity)
	if LastQty != None:
		msg.append_pair(32,LastQty)
	if UnderlyingLastQty != None:
		msg.append_pair(652,UnderlyingLastQty)
	if LastPx != None:
		msg.append_pair(31,LastPx)
	if UnderlyingLastPx != None:
		msg.append_pair(651,UnderlyingLastPx)
	if LastParPx != None:
		msg.append_pair(669,LastParPx)
	if LastSpotRate != None:
		msg.append_pair(194,LastSpotRate)
	if LastForwardPoints != None:
		msg.append_pair(195,LastForwardPoints)
	if LastMkt != None:
		msg.append_pair(30,LastMkt)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if TimeBracket != None:
		msg.append_pair(943,TimeBracket)
	if LastCapacity != None:
		msg.append_pair(29,LastCapacity)
	if DayOrderQty != None:
		msg.append_pair(424,DayOrderQty)
	if DayCumQty != None:
		msg.append_pair(425,DayCumQty)
	if DayAvgPx != None:
		msg.append_pair(426,DayAvgPx)
	if GTBookingInst != None:
		msg.append_pair(427,GTBookingInst)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if ReportToExch != None:
		msg.append_pair(113,ReportToExch)
	if GrossTradeAmt != None:
		msg.append_pair(381,GrossTradeAmt)
	if NumDaysInterest != None:
		msg.append_pair(157,NumDaysInterest)
	if ExDate != None:
		msg.append_pair(230,ExDate)
	if AccruedInterestRate != None:
		msg.append_pair(158,AccruedInterestRate)
	if AccruedInterestAmt != None:
		msg.append_pair(159,AccruedInterestAmt)
	if InterestAtMaturity != None:
		msg.append_pair(738,InterestAtMaturity)
	if EndAccruedInterestAmt != None:
		msg.append_pair(920,EndAccruedInterestAmt)
	if StartCash != None:
		msg.append_pair(921,StartCash)
	if EndCash != None:
		msg.append_pair(922,EndCash)
	if TradedFlatSwitch != None:
		msg.append_pair(258,TradedFlatSwitch)
	if BasisFeatureDate != None:
		msg.append_pair(259,BasisFeatureDate)
	if BasisFeaturePrice != None:
		msg.append_pair(260,BasisFeaturePrice)
	if Concession != None:
		msg.append_pair(238,Concession)
	if TotalTakedown != None:
		msg.append_pair(237,TotalTakedown)
	if NetMoney != None:
		msg.append_pair(118,NetMoney)
	if SettlCurrAmt != None:
		msg.append_pair(119,SettlCurrAmt)
	if SettlCurrency != None:
		msg.append_pair(120,SettlCurrency)
	if SettlCurrFxRate != None:
		msg.append_pair(155,SettlCurrFxRate)
	if SettlCurrFxRateCalc != None:
		msg.append_pair(156,SettlCurrFxRateCalc)
	if HandlInst != None:
		msg.append_pair(21,HandlInst)
	if MinQty != None:
		msg.append_pair(110,MinQty)
	if MaxFloor != None:
		msg.append_pair(111,MaxFloor)
	if PositionEffect != None:
		msg.append_pair(77,PositionEffect)
	if MaxShow != None:
		msg.append_pair(210,MaxShow)
	if BookingType != None:
		msg.append_pair(775,BookingType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if SettlDate2 != None:
		msg.append_pair(193,SettlDate2)
	if OrderQty2 != None:
		msg.append_pair(192,OrderQty2)
	if LastForwardPoints2 != None:
		msg.append_pair(641,LastForwardPoints2)
	if MultiLegReportingType != None:
		msg.append_pair(442,MultiLegReportingType)
	if CancellationRights != None:
		msg.append_pair(480,CancellationRights)
	if MoneyLaunderingStatus != None:
		msg.append_pair(481,MoneyLaunderingStatus)
	if RegistID != None:
		msg.append_pair(513,RegistID)
	if Designation != None:
		msg.append_pair(494,Designation)
	if TransBkdTime != None:
		msg.append_pair(483,TransBkdTime)
	if ExecValuationPoint != None:
		msg.append_pair(515,ExecValuationPoint)
	if ExecPriceType != None:
		msg.append_pair(484,ExecPriceType)
	if ExecPriceAdjustment != None:
		msg.append_pair(485,ExecPriceAdjustment)
	if PriorityIndicator != None:
		msg.append_pair(638,PriorityIndicator)
	if PriceImprovement != None:
		msg.append_pair(639,PriceImprovement)
	if LastLiquidityInd != None:
		msg.append_pair(851,LastLiquidityInd)
	if CopyMsgIndicator != None:
		msg.append_pair(797,CopyMsgIndicator)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ContraGrp != None:
		for tv in ContraGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if OrderQtyData != None:
		for tv in OrderQtyData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PegInstructions != None:
		for tv in PegInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if DiscretionInstructions != None:
		for tv in DiscretionInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if CommissionData != None:
		for tv in CommissionData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ContAmtGrp != None:
		for tv in ContAmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegExecGrp != None:
		for tv in InstrmtLegExecGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if MiscFeesGrp != None:
		for tv in MiscFeesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def OrderCancelReject(MsgSeqNum,TargetCompID,OrderID,ClOrdID,OrigClOrdID,OrdStatus,CxlRejResponseTo,SecondaryOrderID=None,SecondaryClOrdID=None,ClOrdLinkID=None,WorkingIndicator=None,OrigOrdModTime=None,ListID=None,Account=None,AcctIDSource=None,AccountType=None,TradeOriginationDate=None,TradeDate=None,TransactTime=None,CxlRejReason=None,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,9,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(37,OrderID)
	msg.append_pair(11,ClOrdID)
	msg.append_pair(41,OrigClOrdID)
	msg.append_pair(39,OrdStatus)
	msg.append_pair(434,CxlRejResponseTo)
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if ClOrdLinkID != None:
		msg.append_pair(583,ClOrdLinkID)
	if WorkingIndicator != None:
		msg.append_pair(636,WorkingIndicator)
	if OrigOrdModTime != None:
		msg.append_pair(586,OrigOrdModTime)
	if ListID != None:
		msg.append_pair(66,ListID)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if TradeOriginationDate != None:
		msg.append_pair(229,TradeOriginationDate)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if CxlRejReason != None:
		msg.append_pair(102,CxlRejReason)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def Logon(MsgSeqNum,TargetCompID,EncryptMethod,HeartBtInt,RawDataLength=None,RawData=None,ResetSeqNumFlag=None,NextExpectedMsgSeqNum=None,MaxMessageSize=None,TestMessageIndicator=None,Username=None,Password=None,NoMsgTypes=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,A,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(98,EncryptMethod)
	msg.append_pair(108,HeartBtInt)
	if RawDataLength != None:
		msg.append_pair(95,RawDataLength)
	if RawData != None:
		msg.append_pair(96,RawData)
	if ResetSeqNumFlag != None:
		msg.append_pair(141,ResetSeqNumFlag)
	if NextExpectedMsgSeqNum != None:
		msg.append_pair(789,NextExpectedMsgSeqNum)
	if MaxMessageSize != None:
		msg.append_pair(383,MaxMessageSize)
	if TestMessageIndicator != None:
		msg.append_pair(464,TestMessageIndicator)
	if Username != None:
		msg.append_pair(553,Username)
	if Password != None:
		msg.append_pair(554,Password)
	if NoMsgTypes != None:
		self.tag_vals.append((384,len(NoMsgTypes)-1))
		for i in range(1,len(NoMsgTypes)):
			for idx,attr in enumerate(NoMsgTypes[0]):
				if attr in components_names:
					for tv in attr.tag_vals:
						msg.append_pair(tv[0],tv[1])
				else:
					msg.append_pair(tag_name_to_num[attr],NoMsgTypes[i][idx])
	return msg.encode()

def News(MsgSeqNum,TargetCompID,Headline,LinesOfTextGrp,OrigTime=None,Urgency=None,EncodedHeadlineLen=None,EncodedHeadline=None,URLLink=None,RawDataLength=None,RawData=None,RoutingGrp=None,InstrmtGrp=None,InstrmtLegGrp=None,UndInstrmtGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,B,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(148,Headline)
	for tv in LinesOfTextGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if OrigTime != None:
		msg.append_pair(42,OrigTime)
	if Urgency != None:
		msg.append_pair(61,Urgency)
	if EncodedHeadlineLen != None:
		msg.append_pair(358,EncodedHeadlineLen)
	if EncodedHeadline != None:
		msg.append_pair(359,EncodedHeadline)
	if URLLink != None:
		msg.append_pair(149,URLLink)
	if RawDataLength != None:
		msg.append_pair(95,RawDataLength)
	if RawData != None:
		msg.append_pair(96,RawData)
	if RoutingGrp != None:
		for tv in RoutingGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtGrp != None:
		for tv in InstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def Email(MsgSeqNum,TargetCompID,EmailThreadID,EmailType,Subject,LinesOfTextGrp,OrigTime=None,EncodedSubjectLen=None,EncodedSubject=None,OrderID=None,ClOrdID=None,RawDataLength=None,RawData=None,RoutingGrp=None,InstrmtGrp=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,C,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(164,EmailThreadID)
	msg.append_pair(94,EmailType)
	msg.append_pair(147,Subject)
	for tv in LinesOfTextGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if OrigTime != None:
		msg.append_pair(42,OrigTime)
	if EncodedSubjectLen != None:
		msg.append_pair(356,EncodedSubjectLen)
	if EncodedSubject != None:
		msg.append_pair(357,EncodedSubject)
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if RawDataLength != None:
		msg.append_pair(95,RawDataLength)
	if RawData != None:
		msg.append_pair(96,RawData)
	if RoutingGrp != None:
		for tv in RoutingGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtGrp != None:
		for tv in InstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def NewOrderSingle(MsgSeqNum,TargetCompID,ClOrdID,Side,TransactTime,OrdType,Instrument,OrderQtyData,SecondaryClOrdID=None,ClOrdLinkID=None,TradeOriginationDate=None,TradeDate=None,Account=None,AcctIDSource=None,AccountType=None,DayBookingInst=None,BookingUnit=None,PreallocMethod=None,AllocID=None,SettlType=None,SettlDate=None,CashMargin=None,ClearingFeeIndicator=None,HandlInst=None,ExecInst=None,MinQty=None,MaxFloor=None,ExDestination=None,ProcessCode=None,PrevClosePx=None,LocateReqd=None,QtyType=None,PriceType=None,Price=None,StopPx=None,Currency=None,ComplianceID=None,SolicitedFlag=None,IOIID=None,QuoteID=None,TimeInForce=None,EffectiveTime=None,ExpireDate=None,ExpireTime=None,GTBookingInst=None,OrderCapacity=None,OrderRestrictions=None,CustOrderCapacity=None,ForexReq=None,SettlCurrency=None,BookingType=None,Text=None,EncodedTextLen=None,EncodedText=None,SettlDate2=None,OrderQty2=None,Price2=None,PositionEffect=None,CoveredOrUncovered=None,MaxShow=None,TargetStrategy=None,TargetStrategyParameters=None,ParticipationRate=None,CancellationRights=None,MoneyLaunderingStatus=None,RegistID=None,Designation=None,Parties=None,PreAllocGrp=None,TrdgSesGrp=None,FinancingDetails=None,UndInstrmtGrp=None,Stipulations=None,SpreadOrBenchmarkCurveData=None,YieldData=None,CommissionData=None,PegInstructions=None,DiscretionInstructions=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,D,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(11,ClOrdID)
	msg.append_pair(54,Side)
	msg.append_pair(60,TransactTime)
	msg.append_pair(40,OrdType)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in OrderQtyData.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if ClOrdLinkID != None:
		msg.append_pair(583,ClOrdLinkID)
	if TradeOriginationDate != None:
		msg.append_pair(229,TradeOriginationDate)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if DayBookingInst != None:
		msg.append_pair(589,DayBookingInst)
	if BookingUnit != None:
		msg.append_pair(590,BookingUnit)
	if PreallocMethod != None:
		msg.append_pair(591,PreallocMethod)
	if AllocID != None:
		msg.append_pair(70,AllocID)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if CashMargin != None:
		msg.append_pair(544,CashMargin)
	if ClearingFeeIndicator != None:
		msg.append_pair(635,ClearingFeeIndicator)
	if HandlInst != None:
		msg.append_pair(21,HandlInst)
	if ExecInst != None:
		msg.append_pair(18,ExecInst)
	if MinQty != None:
		msg.append_pair(110,MinQty)
	if MaxFloor != None:
		msg.append_pair(111,MaxFloor)
	if ExDestination != None:
		msg.append_pair(100,ExDestination)
	if ProcessCode != None:
		msg.append_pair(81,ProcessCode)
	if PrevClosePx != None:
		msg.append_pair(140,PrevClosePx)
	if LocateReqd != None:
		msg.append_pair(114,LocateReqd)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if Price != None:
		msg.append_pair(44,Price)
	if StopPx != None:
		msg.append_pair(99,StopPx)
	if Currency != None:
		msg.append_pair(15,Currency)
	if ComplianceID != None:
		msg.append_pair(376,ComplianceID)
	if SolicitedFlag != None:
		msg.append_pair(377,SolicitedFlag)
	if IOIID != None:
		msg.append_pair(23,IOIID)
	if QuoteID != None:
		msg.append_pair(117,QuoteID)
	if TimeInForce != None:
		msg.append_pair(59,TimeInForce)
	if EffectiveTime != None:
		msg.append_pair(168,EffectiveTime)
	if ExpireDate != None:
		msg.append_pair(432,ExpireDate)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if GTBookingInst != None:
		msg.append_pair(427,GTBookingInst)
	if OrderCapacity != None:
		msg.append_pair(528,OrderCapacity)
	if OrderRestrictions != None:
		msg.append_pair(529,OrderRestrictions)
	if CustOrderCapacity != None:
		msg.append_pair(582,CustOrderCapacity)
	if ForexReq != None:
		msg.append_pair(121,ForexReq)
	if SettlCurrency != None:
		msg.append_pair(120,SettlCurrency)
	if BookingType != None:
		msg.append_pair(775,BookingType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if SettlDate2 != None:
		msg.append_pair(193,SettlDate2)
	if OrderQty2 != None:
		msg.append_pair(192,OrderQty2)
	if Price2 != None:
		msg.append_pair(640,Price2)
	if PositionEffect != None:
		msg.append_pair(77,PositionEffect)
	if CoveredOrUncovered != None:
		msg.append_pair(203,CoveredOrUncovered)
	if MaxShow != None:
		msg.append_pair(210,MaxShow)
	if TargetStrategy != None:
		msg.append_pair(847,TargetStrategy)
	if TargetStrategyParameters != None:
		msg.append_pair(848,TargetStrategyParameters)
	if ParticipationRate != None:
		msg.append_pair(849,ParticipationRate)
	if CancellationRights != None:
		msg.append_pair(480,CancellationRights)
	if MoneyLaunderingStatus != None:
		msg.append_pair(481,MoneyLaunderingStatus)
	if RegistID != None:
		msg.append_pair(513,RegistID)
	if Designation != None:
		msg.append_pair(494,Designation)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PreAllocGrp != None:
		for tv in PreAllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if CommissionData != None:
		for tv in CommissionData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PegInstructions != None:
		for tv in PegInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if DiscretionInstructions != None:
		for tv in DiscretionInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def NewOrderList(MsgSeqNum,TargetCompID,ListID,BidType,TotNoOrders,ListOrdGrp,BidID=None,ClientBidID=None,ProgRptReqs=None,ProgPeriodInterval=None,CancellationRights=None,MoneyLaunderingStatus=None,RegistID=None,ListExecInstType=None,ListExecInst=None,EncodedListExecInstLen=None,EncodedListExecInst=None,AllowableOneSidednessPct=None,AllowableOneSidednessValue=None,AllowableOneSidednessCurr=None,LastFragment=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,E,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(66,ListID)
	msg.append_pair(394,BidType)
	msg.append_pair(68,TotNoOrders)
	for tv in ListOrdGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if BidID != None:
		msg.append_pair(390,BidID)
	if ClientBidID != None:
		msg.append_pair(391,ClientBidID)
	if ProgRptReqs != None:
		msg.append_pair(414,ProgRptReqs)
	if ProgPeriodInterval != None:
		msg.append_pair(415,ProgPeriodInterval)
	if CancellationRights != None:
		msg.append_pair(480,CancellationRights)
	if MoneyLaunderingStatus != None:
		msg.append_pair(481,MoneyLaunderingStatus)
	if RegistID != None:
		msg.append_pair(513,RegistID)
	if ListExecInstType != None:
		msg.append_pair(433,ListExecInstType)
	if ListExecInst != None:
		msg.append_pair(69,ListExecInst)
	if EncodedListExecInstLen != None:
		msg.append_pair(352,EncodedListExecInstLen)
	if EncodedListExecInst != None:
		msg.append_pair(353,EncodedListExecInst)
	if AllowableOneSidednessPct != None:
		msg.append_pair(765,AllowableOneSidednessPct)
	if AllowableOneSidednessValue != None:
		msg.append_pair(766,AllowableOneSidednessValue)
	if AllowableOneSidednessCurr != None:
		msg.append_pair(767,AllowableOneSidednessCurr)
	if LastFragment != None:
		msg.append_pair(893,LastFragment)
	return msg.encode()

def OrderCancelRequest(MsgSeqNum,TargetCompID,OrigClOrdID,ClOrdID,Side,TransactTime,Instrument,OrderQtyData,OrderID=None,SecondaryClOrdID=None,ClOrdLinkID=None,ListID=None,OrigOrdModTime=None,Account=None,AcctIDSource=None,AccountType=None,ComplianceID=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,FinancingDetails=None,UndInstrmtGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,F,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(41,OrigClOrdID)
	msg.append_pair(11,ClOrdID)
	msg.append_pair(54,Side)
	msg.append_pair(60,TransactTime)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in OrderQtyData.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if ClOrdLinkID != None:
		msg.append_pair(583,ClOrdLinkID)
	if ListID != None:
		msg.append_pair(66,ListID)
	if OrigOrdModTime != None:
		msg.append_pair(586,OrigOrdModTime)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if ComplianceID != None:
		msg.append_pair(376,ComplianceID)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def OrderCancelReplaceRequest(MsgSeqNum,TargetCompID,OrigClOrdID,ClOrdID,Side,TransactTime,OrdType,Instrument,OrderQtyData,OrderID=None,TradeOriginationDate=None,TradeDate=None,SecondaryClOrdID=None,ClOrdLinkID=None,ListID=None,OrigOrdModTime=None,Account=None,AcctIDSource=None,AccountType=None,DayBookingInst=None,BookingUnit=None,PreallocMethod=None,AllocID=None,SettlType=None,SettlDate=None,CashMargin=None,ClearingFeeIndicator=None,HandlInst=None,ExecInst=None,MinQty=None,MaxFloor=None,ExDestination=None,QtyType=None,PriceType=None,Price=None,StopPx=None,TargetStrategy=None,TargetStrategyParameters=None,ParticipationRate=None,ComplianceID=None,SolicitedFlag=None,Currency=None,TimeInForce=None,EffectiveTime=None,ExpireDate=None,ExpireTime=None,GTBookingInst=None,OrderCapacity=None,OrderRestrictions=None,CustOrderCapacity=None,ForexReq=None,SettlCurrency=None,BookingType=None,Text=None,EncodedTextLen=None,EncodedText=None,SettlDate2=None,OrderQty2=None,Price2=None,PositionEffect=None,CoveredOrUncovered=None,MaxShow=None,LocateReqd=None,CancellationRights=None,MoneyLaunderingStatus=None,RegistID=None,Designation=None,Parties=None,PreAllocGrp=None,TrdgSesGrp=None,FinancingDetails=None,UndInstrmtGrp=None,SpreadOrBenchmarkCurveData=None,YieldData=None,PegInstructions=None,DiscretionInstructions=None,CommissionData=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,G,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(41,OrigClOrdID)
	msg.append_pair(11,ClOrdID)
	msg.append_pair(54,Side)
	msg.append_pair(60,TransactTime)
	msg.append_pair(40,OrdType)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in OrderQtyData.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if TradeOriginationDate != None:
		msg.append_pair(229,TradeOriginationDate)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if ClOrdLinkID != None:
		msg.append_pair(583,ClOrdLinkID)
	if ListID != None:
		msg.append_pair(66,ListID)
	if OrigOrdModTime != None:
		msg.append_pair(586,OrigOrdModTime)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if DayBookingInst != None:
		msg.append_pair(589,DayBookingInst)
	if BookingUnit != None:
		msg.append_pair(590,BookingUnit)
	if PreallocMethod != None:
		msg.append_pair(591,PreallocMethod)
	if AllocID != None:
		msg.append_pair(70,AllocID)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if CashMargin != None:
		msg.append_pair(544,CashMargin)
	if ClearingFeeIndicator != None:
		msg.append_pair(635,ClearingFeeIndicator)
	if HandlInst != None:
		msg.append_pair(21,HandlInst)
	if ExecInst != None:
		msg.append_pair(18,ExecInst)
	if MinQty != None:
		msg.append_pair(110,MinQty)
	if MaxFloor != None:
		msg.append_pair(111,MaxFloor)
	if ExDestination != None:
		msg.append_pair(100,ExDestination)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if Price != None:
		msg.append_pair(44,Price)
	if StopPx != None:
		msg.append_pair(99,StopPx)
	if TargetStrategy != None:
		msg.append_pair(847,TargetStrategy)
	if TargetStrategyParameters != None:
		msg.append_pair(848,TargetStrategyParameters)
	if ParticipationRate != None:
		msg.append_pair(849,ParticipationRate)
	if ComplianceID != None:
		msg.append_pair(376,ComplianceID)
	if SolicitedFlag != None:
		msg.append_pair(377,SolicitedFlag)
	if Currency != None:
		msg.append_pair(15,Currency)
	if TimeInForce != None:
		msg.append_pair(59,TimeInForce)
	if EffectiveTime != None:
		msg.append_pair(168,EffectiveTime)
	if ExpireDate != None:
		msg.append_pair(432,ExpireDate)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if GTBookingInst != None:
		msg.append_pair(427,GTBookingInst)
	if OrderCapacity != None:
		msg.append_pair(528,OrderCapacity)
	if OrderRestrictions != None:
		msg.append_pair(529,OrderRestrictions)
	if CustOrderCapacity != None:
		msg.append_pair(582,CustOrderCapacity)
	if ForexReq != None:
		msg.append_pair(121,ForexReq)
	if SettlCurrency != None:
		msg.append_pair(120,SettlCurrency)
	if BookingType != None:
		msg.append_pair(775,BookingType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if SettlDate2 != None:
		msg.append_pair(193,SettlDate2)
	if OrderQty2 != None:
		msg.append_pair(192,OrderQty2)
	if Price2 != None:
		msg.append_pair(640,Price2)
	if PositionEffect != None:
		msg.append_pair(77,PositionEffect)
	if CoveredOrUncovered != None:
		msg.append_pair(203,CoveredOrUncovered)
	if MaxShow != None:
		msg.append_pair(210,MaxShow)
	if LocateReqd != None:
		msg.append_pair(114,LocateReqd)
	if CancellationRights != None:
		msg.append_pair(480,CancellationRights)
	if MoneyLaunderingStatus != None:
		msg.append_pair(481,MoneyLaunderingStatus)
	if RegistID != None:
		msg.append_pair(513,RegistID)
	if Designation != None:
		msg.append_pair(494,Designation)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PreAllocGrp != None:
		for tv in PreAllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PegInstructions != None:
		for tv in PegInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if DiscretionInstructions != None:
		for tv in DiscretionInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if CommissionData != None:
		for tv in CommissionData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def OrderStatusRequest(MsgSeqNum,TargetCompID,ClOrdID,Side,Instrument,OrderID=None,SecondaryClOrdID=None,ClOrdLinkID=None,OrdStatusReqID=None,Account=None,AcctIDSource=None,Parties=None,FinancingDetails=None,UndInstrmtGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,H,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(11,ClOrdID)
	msg.append_pair(54,Side)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if ClOrdLinkID != None:
		msg.append_pair(583,ClOrdLinkID)
	if OrdStatusReqID != None:
		msg.append_pair(790,OrdStatusReqID)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def AllocationInstruction(MsgSeqNum,TargetCompID,AllocID,AllocTransType,AllocType,AllocNoOrdersType,Side,Quantity,AvgPx,TradeDate,Instrument,SecondaryAllocID=None,RefAllocID=None,AllocCancReplaceReason=None,AllocIntermedReqType=None,AllocLinkID=None,AllocLinkType=None,BookingRefID=None,PreviouslyReported=None,ReversalIndicator=None,MatchType=None,QtyType=None,LastMkt=None,TradeOriginationDate=None,TradingSessionID=None,TradingSessionSubID=None,PriceType=None,AvgParPx=None,Currency=None,AvgPxPrecision=None,TransactTime=None,SettlType=None,SettlDate=None,BookingType=None,GrossTradeAmt=None,Concession=None,TotalTakedown=None,NetMoney=None,PositionEffect=None,AutoAcceptIndicator=None,Text=None,EncodedTextLen=None,EncodedText=None,NumDaysInterest=None,AccruedInterestRate=None,AccruedInterestAmt=None,TotalAccruedInterestAmt=None,InterestAtMaturity=None,EndAccruedInterestAmt=None,StartCash=None,EndCash=None,LegalConfirm=None,TotNoAllocs=None,LastFragment=None,OrdAllocGrp=None,ExecAllocGrp=None,InstrumentExtension=None,FinancingDetails=None,UndInstrmtGrp=None,InstrmtLegGrp=None,SpreadOrBenchmarkCurveData=None,Parties=None,Stipulations=None,YieldData=None,AllocGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,J,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(70,AllocID)
	msg.append_pair(71,AllocTransType)
	msg.append_pair(626,AllocType)
	msg.append_pair(857,AllocNoOrdersType)
	msg.append_pair(54,Side)
	msg.append_pair(53,Quantity)
	msg.append_pair(6,AvgPx)
	msg.append_pair(75,TradeDate)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if SecondaryAllocID != None:
		msg.append_pair(793,SecondaryAllocID)
	if RefAllocID != None:
		msg.append_pair(72,RefAllocID)
	if AllocCancReplaceReason != None:
		msg.append_pair(796,AllocCancReplaceReason)
	if AllocIntermedReqType != None:
		msg.append_pair(808,AllocIntermedReqType)
	if AllocLinkID != None:
		msg.append_pair(196,AllocLinkID)
	if AllocLinkType != None:
		msg.append_pair(197,AllocLinkType)
	if BookingRefID != None:
		msg.append_pair(466,BookingRefID)
	if PreviouslyReported != None:
		msg.append_pair(570,PreviouslyReported)
	if ReversalIndicator != None:
		msg.append_pair(700,ReversalIndicator)
	if MatchType != None:
		msg.append_pair(574,MatchType)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if LastMkt != None:
		msg.append_pair(30,LastMkt)
	if TradeOriginationDate != None:
		msg.append_pair(229,TradeOriginationDate)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if AvgParPx != None:
		msg.append_pair(860,AvgParPx)
	if Currency != None:
		msg.append_pair(15,Currency)
	if AvgPxPrecision != None:
		msg.append_pair(74,AvgPxPrecision)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if BookingType != None:
		msg.append_pair(775,BookingType)
	if GrossTradeAmt != None:
		msg.append_pair(381,GrossTradeAmt)
	if Concession != None:
		msg.append_pair(238,Concession)
	if TotalTakedown != None:
		msg.append_pair(237,TotalTakedown)
	if NetMoney != None:
		msg.append_pair(118,NetMoney)
	if PositionEffect != None:
		msg.append_pair(77,PositionEffect)
	if AutoAcceptIndicator != None:
		msg.append_pair(754,AutoAcceptIndicator)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if NumDaysInterest != None:
		msg.append_pair(157,NumDaysInterest)
	if AccruedInterestRate != None:
		msg.append_pair(158,AccruedInterestRate)
	if AccruedInterestAmt != None:
		msg.append_pair(159,AccruedInterestAmt)
	if TotalAccruedInterestAmt != None:
		msg.append_pair(540,TotalAccruedInterestAmt)
	if InterestAtMaturity != None:
		msg.append_pair(738,InterestAtMaturity)
	if EndAccruedInterestAmt != None:
		msg.append_pair(920,EndAccruedInterestAmt)
	if StartCash != None:
		msg.append_pair(921,StartCash)
	if EndCash != None:
		msg.append_pair(922,EndCash)
	if LegalConfirm != None:
		msg.append_pair(650,LegalConfirm)
	if TotNoAllocs != None:
		msg.append_pair(892,TotNoAllocs)
	if LastFragment != None:
		msg.append_pair(893,LastFragment)
	if OrdAllocGrp != None:
		for tv in OrdAllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ExecAllocGrp != None:
		for tv in ExecAllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrumentExtension != None:
		for tv in InstrumentExtension.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if AllocGrp != None:
		for tv in AllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def ListCancelRequest(MsgSeqNum,TargetCompID,ListID,TransactTime,TradeOriginationDate=None,TradeDate=None,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,K,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(66,ListID)
	msg.append_pair(60,TransactTime)
	if TradeOriginationDate != None:
		msg.append_pair(229,TradeOriginationDate)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def ListExecute(MsgSeqNum,TargetCompID,ListID,TransactTime,ClientBidID=None,BidID=None,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,L,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(66,ListID)
	msg.append_pair(60,TransactTime)
	if ClientBidID != None:
		msg.append_pair(391,ClientBidID)
	if BidID != None:
		msg.append_pair(390,BidID)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def ListStatusRequest(MsgSeqNum,TargetCompID,ListID,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,M,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(66,ListID)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def ListStatus(MsgSeqNum,TargetCompID,ListID,ListStatusType,NoRpts,ListOrderStatus,RptSeq,TotNoOrders,OrdListStatGrp,ListStatusText=None,EncodedListStatusTextLen=None,EncodedListStatusText=None,TransactTime=None,LastFragment=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,N,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(66,ListID)
	msg.append_pair(429,ListStatusType)
	msg.append_pair(82,NoRpts)
	msg.append_pair(431,ListOrderStatus)
	msg.append_pair(83,RptSeq)
	msg.append_pair(68,TotNoOrders)
	for tv in OrdListStatGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if ListStatusText != None:
		msg.append_pair(444,ListStatusText)
	if EncodedListStatusTextLen != None:
		msg.append_pair(445,EncodedListStatusTextLen)
	if EncodedListStatusText != None:
		msg.append_pair(446,EncodedListStatusText)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if LastFragment != None:
		msg.append_pair(893,LastFragment)
	return msg.encode()

def AllocationInstructionAck(MsgSeqNum,TargetCompID,AllocID,TransactTime,AllocStatus,SecondaryAllocID=None,TradeDate=None,AllocRejCode=None,AllocType=None,AllocIntermedReqType=None,MatchStatus=None,Product=None,SecurityType=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,AllocAckGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,P,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(70,AllocID)
	msg.append_pair(60,TransactTime)
	msg.append_pair(87,AllocStatus)
	if SecondaryAllocID != None:
		msg.append_pair(793,SecondaryAllocID)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if AllocRejCode != None:
		msg.append_pair(88,AllocRejCode)
	if AllocType != None:
		msg.append_pair(626,AllocType)
	if AllocIntermedReqType != None:
		msg.append_pair(808,AllocIntermedReqType)
	if MatchStatus != None:
		msg.append_pair(573,MatchStatus)
	if Product != None:
		msg.append_pair(460,Product)
	if SecurityType != None:
		msg.append_pair(167,SecurityType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if AllocAckGrp != None:
		for tv in AllocAckGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def DontKnowTrade(MsgSeqNum,TargetCompID,OrderID,ExecID,DKReason,Side,Instrument,OrderQtyData,SecondaryOrderID=None,LastQty=None,LastPx=None,Text=None,EncodedTextLen=None,EncodedText=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,Q,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(37,OrderID)
	msg.append_pair(17,ExecID)
	msg.append_pair(127,DKReason)
	msg.append_pair(54,Side)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in OrderQtyData.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if LastQty != None:
		msg.append_pair(32,LastQty)
	if LastPx != None:
		msg.append_pair(31,LastPx)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def QuoteRequest(MsgSeqNum,TargetCompID,QuoteReqID,QuotReqGrp,RFQReqID=None,ClOrdID=None,OrderCapacity=None,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,R,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(131,QuoteReqID)
	for tv in QuotReqGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if RFQReqID != None:
		msg.append_pair(644,RFQReqID)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if OrderCapacity != None:
		msg.append_pair(528,OrderCapacity)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def Quote(MsgSeqNum,TargetCompID,QuoteID,Instrument,QuoteReqID=None,QuoteRespID=None,QuoteType=None,QuoteResponseLevel=None,TradingSessionID=None,TradingSessionSubID=None,Side=None,SettlType=None,SettlDate=None,SettlDate2=None,OrderQty2=None,Currency=None,Account=None,AcctIDSource=None,AccountType=None,BidPx=None,OfferPx=None,MktBidPx=None,MktOfferPx=None,MinBidSize=None,BidSize=None,MinOfferSize=None,OfferSize=None,ValidUntilTime=None,BidSpotRate=None,OfferSpotRate=None,BidForwardPoints=None,OfferForwardPoints=None,MidPx=None,BidYield=None,MidYield=None,OfferYield=None,TransactTime=None,OrdType=None,BidForwardPoints2=None,OfferForwardPoints2=None,SettlCurrBidFxRate=None,SettlCurrOfferFxRate=None,SettlCurrFxRateCalc=None,CommType=None,Commission=None,CustOrderCapacity=None,ExDestination=None,OrderCapacity=None,PriceType=None,Text=None,EncodedTextLen=None,EncodedText=None,QuotQualGrp=None,Parties=None,FinancingDetails=None,UndInstrmtGrp=None,OrderQtyData=None,Stipulations=None,LegQuotGrp=None,SpreadOrBenchmarkCurveData=None,YieldData=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,S,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(117,QuoteID)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if QuoteReqID != None:
		msg.append_pair(131,QuoteReqID)
	if QuoteRespID != None:
		msg.append_pair(693,QuoteRespID)
	if QuoteType != None:
		msg.append_pair(537,QuoteType)
	if QuoteResponseLevel != None:
		msg.append_pair(301,QuoteResponseLevel)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if Side != None:
		msg.append_pair(54,Side)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if SettlDate2 != None:
		msg.append_pair(193,SettlDate2)
	if OrderQty2 != None:
		msg.append_pair(192,OrderQty2)
	if Currency != None:
		msg.append_pair(15,Currency)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if BidPx != None:
		msg.append_pair(132,BidPx)
	if OfferPx != None:
		msg.append_pair(133,OfferPx)
	if MktBidPx != None:
		msg.append_pair(645,MktBidPx)
	if MktOfferPx != None:
		msg.append_pair(646,MktOfferPx)
	if MinBidSize != None:
		msg.append_pair(647,MinBidSize)
	if BidSize != None:
		msg.append_pair(134,BidSize)
	if MinOfferSize != None:
		msg.append_pair(648,MinOfferSize)
	if OfferSize != None:
		msg.append_pair(135,OfferSize)
	if ValidUntilTime != None:
		msg.append_pair(62,ValidUntilTime)
	if BidSpotRate != None:
		msg.append_pair(188,BidSpotRate)
	if OfferSpotRate != None:
		msg.append_pair(190,OfferSpotRate)
	if BidForwardPoints != None:
		msg.append_pair(189,BidForwardPoints)
	if OfferForwardPoints != None:
		msg.append_pair(191,OfferForwardPoints)
	if MidPx != None:
		msg.append_pair(631,MidPx)
	if BidYield != None:
		msg.append_pair(632,BidYield)
	if MidYield != None:
		msg.append_pair(633,MidYield)
	if OfferYield != None:
		msg.append_pair(634,OfferYield)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if OrdType != None:
		msg.append_pair(40,OrdType)
	if BidForwardPoints2 != None:
		msg.append_pair(642,BidForwardPoints2)
	if OfferForwardPoints2 != None:
		msg.append_pair(643,OfferForwardPoints2)
	if SettlCurrBidFxRate != None:
		msg.append_pair(656,SettlCurrBidFxRate)
	if SettlCurrOfferFxRate != None:
		msg.append_pair(657,SettlCurrOfferFxRate)
	if SettlCurrFxRateCalc != None:
		msg.append_pair(156,SettlCurrFxRateCalc)
	if CommType != None:
		msg.append_pair(13,CommType)
	if Commission != None:
		msg.append_pair(12,Commission)
	if CustOrderCapacity != None:
		msg.append_pair(582,CustOrderCapacity)
	if ExDestination != None:
		msg.append_pair(100,ExDestination)
	if OrderCapacity != None:
		msg.append_pair(528,OrderCapacity)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if QuotQualGrp != None:
		for tv in QuotQualGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if OrderQtyData != None:
		for tv in OrderQtyData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if LegQuotGrp != None:
		for tv in LegQuotGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def SettlementInstructions(MsgSeqNum,TargetCompID,SettlInstMsgID,SettlInstMode,TransactTime,SettlInstReqID=None,SettlInstReqRejCode=None,Text=None,EncodedTextLen=None,EncodedText=None,ClOrdID=None,SettlInstGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,T,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(777,SettlInstMsgID)
	msg.append_pair(160,SettlInstMode)
	msg.append_pair(60,TransactTime)
	if SettlInstReqID != None:
		msg.append_pair(791,SettlInstReqID)
	if SettlInstReqRejCode != None:
		msg.append_pair(792,SettlInstReqRejCode)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if SettlInstGrp != None:
		for tv in SettlInstGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def MarketDataRequest(MsgSeqNum,TargetCompID,MDReqID,SubscriptionRequestType,MarketDepth,MDReqGrp,InstrmtMDReqGrp,MDUpdateType=None,AggregatedBook=None,OpenCloseSettlFlag=None,Scope=None,MDImplicitDelete=None,ApplQueueAction=None,ApplQueueMax=None,TrdgSesGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,V,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(262,MDReqID)
	msg.append_pair(263,SubscriptionRequestType)
	msg.append_pair(264,MarketDepth)
	for tv in MDReqGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in InstrmtMDReqGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if MDUpdateType != None:
		msg.append_pair(265,MDUpdateType)
	if AggregatedBook != None:
		msg.append_pair(266,AggregatedBook)
	if OpenCloseSettlFlag != None:
		msg.append_pair(286,OpenCloseSettlFlag)
	if Scope != None:
		msg.append_pair(546,Scope)
	if MDImplicitDelete != None:
		msg.append_pair(547,MDImplicitDelete)
	if ApplQueueAction != None:
		msg.append_pair(815,ApplQueueAction)
	if ApplQueueMax != None:
		msg.append_pair(812,ApplQueueMax)
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def MarketDataSnapshotFullRefresh(MsgSeqNum,TargetCompID,Instrument,MDFullGrp,MDReqID=None,FinancialStatus=None,CorporateAction=None,NetChgPrevDay=None,ApplQueueDepth=None,ApplQueueResolution=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,W,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in MDFullGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if MDReqID != None:
		msg.append_pair(262,MDReqID)
	if FinancialStatus != None:
		msg.append_pair(291,FinancialStatus)
	if CorporateAction != None:
		msg.append_pair(292,CorporateAction)
	if NetChgPrevDay != None:
		msg.append_pair(451,NetChgPrevDay)
	if ApplQueueDepth != None:
		msg.append_pair(813,ApplQueueDepth)
	if ApplQueueResolution != None:
		msg.append_pair(814,ApplQueueResolution)
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def MarketDataIncrementalRefresh(MsgSeqNum,TargetCompID,MDIncGrp,MDReqID=None,ApplQueueDepth=None,ApplQueueResolution=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,X,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	for tv in MDIncGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if MDReqID != None:
		msg.append_pair(262,MDReqID)
	if ApplQueueDepth != None:
		msg.append_pair(813,ApplQueueDepth)
	if ApplQueueResolution != None:
		msg.append_pair(814,ApplQueueResolution)
	return msg.encode()

def MarketDataRequestReject(MsgSeqNum,TargetCompID,MDReqID,MDReqRejReason=None,Text=None,EncodedTextLen=None,EncodedText=None,MDRjctGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,Y,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(262,MDReqID)
	if MDReqRejReason != None:
		msg.append_pair(281,MDReqRejReason)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if MDRjctGrp != None:
		for tv in MDRjctGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def QuoteCancel(MsgSeqNum,TargetCompID,QuoteID,QuoteCancelType,QuoteReqID=None,QuoteResponseLevel=None,Account=None,AcctIDSource=None,AccountType=None,TradingSessionID=None,TradingSessionSubID=None,Parties=None,QuotCxlEntriesGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,Z,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(117,QuoteID)
	msg.append_pair(298,QuoteCancelType)
	if QuoteReqID != None:
		msg.append_pair(131,QuoteReqID)
	if QuoteResponseLevel != None:
		msg.append_pair(301,QuoteResponseLevel)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if QuotCxlEntriesGrp != None:
		for tv in QuotCxlEntriesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def QuoteStatusRequest(MsgSeqNum,TargetCompID,Instrument,QuoteStatusReqID=None,QuoteID=None,Account=None,AcctIDSource=None,AccountType=None,TradingSessionID=None,TradingSessionSubID=None,SubscriptionRequestType=None,FinancingDetails=None,UndInstrmtGrp=None,InstrmtLegGrp=None,Parties=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,a,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if QuoteStatusReqID != None:
		msg.append_pair(649,QuoteStatusReqID)
	if QuoteID != None:
		msg.append_pair(117,QuoteID)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def MassQuoteAcknowledgement(MsgSeqNum,TargetCompID,QuoteStatus,QuoteReqID=None,QuoteID=None,QuoteRejectReason=None,QuoteResponseLevel=None,QuoteType=None,Account=None,AcctIDSource=None,AccountType=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,QuotSetAckGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,b,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(297,QuoteStatus)
	if QuoteReqID != None:
		msg.append_pair(131,QuoteReqID)
	if QuoteID != None:
		msg.append_pair(117,QuoteID)
	if QuoteRejectReason != None:
		msg.append_pair(300,QuoteRejectReason)
	if QuoteResponseLevel != None:
		msg.append_pair(301,QuoteResponseLevel)
	if QuoteType != None:
		msg.append_pair(537,QuoteType)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if QuotSetAckGrp != None:
		for tv in QuotSetAckGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def SecurityDefinitionRequest(MsgSeqNum,TargetCompID,SecurityReqID,SecurityRequestType,Currency=None,Text=None,EncodedTextLen=None,EncodedText=None,TradingSessionID=None,TradingSessionSubID=None,ExpirationCycle=None,SubscriptionRequestType=None,Instrument=None,InstrumentExtension=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,c,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(320,SecurityReqID)
	msg.append_pair(321,SecurityRequestType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if ExpirationCycle != None:
		msg.append_pair(827,ExpirationCycle)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrumentExtension != None:
		for tv in InstrumentExtension.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def SecurityDefinition(MsgSeqNum,TargetCompID,SecurityReqID,SecurityResponseID,SecurityResponseType,Currency=None,TradingSessionID=None,TradingSessionSubID=None,Text=None,EncodedTextLen=None,EncodedText=None,ExpirationCycle=None,RoundLot=None,MinTradeVol=None,Instrument=None,InstrumentExtension=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,d,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(320,SecurityReqID)
	msg.append_pair(322,SecurityResponseID)
	msg.append_pair(323,SecurityResponseType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if ExpirationCycle != None:
		msg.append_pair(827,ExpirationCycle)
	if RoundLot != None:
		msg.append_pair(561,RoundLot)
	if MinTradeVol != None:
		msg.append_pair(562,MinTradeVol)
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrumentExtension != None:
		for tv in InstrumentExtension.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def SecurityStatusRequest(MsgSeqNum,TargetCompID,SecurityStatusReqID,SubscriptionRequestType,Instrument,Currency=None,TradingSessionID=None,TradingSessionSubID=None,InstrumentExtension=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,e,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(324,SecurityStatusReqID)
	msg.append_pair(263,SubscriptionRequestType)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if Currency != None:
		msg.append_pair(15,Currency)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if InstrumentExtension != None:
		for tv in InstrumentExtension.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def SecurityStatus(MsgSeqNum,TargetCompID,Instrument,SecurityStatusReqID=None,Currency=None,TradingSessionID=None,TradingSessionSubID=None,UnsolicitedIndicator=None,SecurityTradingStatus=None,FinancialStatus=None,CorporateAction=None,HaltReasonChar=None,InViewOfCommon=None,DueToRelated=None,BuyVolume=None,SellVolume=None,HighPx=None,LowPx=None,LastPx=None,TransactTime=None,Adjustment=None,Text=None,EncodedTextLen=None,EncodedText=None,InstrumentExtension=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,f,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if SecurityStatusReqID != None:
		msg.append_pair(324,SecurityStatusReqID)
	if Currency != None:
		msg.append_pair(15,Currency)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if UnsolicitedIndicator != None:
		msg.append_pair(325,UnsolicitedIndicator)
	if SecurityTradingStatus != None:
		msg.append_pair(326,SecurityTradingStatus)
	if FinancialStatus != None:
		msg.append_pair(291,FinancialStatus)
	if CorporateAction != None:
		msg.append_pair(292,CorporateAction)
	if HaltReasonChar != None:
		msg.append_pair(327,HaltReasonChar)
	if InViewOfCommon != None:
		msg.append_pair(328,InViewOfCommon)
	if DueToRelated != None:
		msg.append_pair(329,DueToRelated)
	if BuyVolume != None:
		msg.append_pair(330,BuyVolume)
	if SellVolume != None:
		msg.append_pair(331,SellVolume)
	if HighPx != None:
		msg.append_pair(332,HighPx)
	if LowPx != None:
		msg.append_pair(333,LowPx)
	if LastPx != None:
		msg.append_pair(31,LastPx)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if Adjustment != None:
		msg.append_pair(334,Adjustment)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if InstrumentExtension != None:
		for tv in InstrumentExtension.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def TradingSessionStatusRequest(MsgSeqNum,TargetCompID,TradSesReqID,SubscriptionRequestType,TradingSessionID=None,TradingSessionSubID=None,TradSesMethod=None,TradSesMode=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,g,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(335,TradSesReqID)
	msg.append_pair(263,SubscriptionRequestType)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if TradSesMethod != None:
		msg.append_pair(338,TradSesMethod)
	if TradSesMode != None:
		msg.append_pair(339,TradSesMode)
	return msg.encode()

def TradingSessionStatus(MsgSeqNum,TargetCompID,TradingSessionID,TradSesStatus,TradSesReqID=None,TradingSessionSubID=None,TradSesMethod=None,TradSesMode=None,UnsolicitedIndicator=None,TradSesStatusRejReason=None,TradSesStartTime=None,TradSesOpenTime=None,TradSesPreCloseTime=None,TradSesCloseTime=None,TradSesEndTime=None,TotalVolumeTraded=None,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,h,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(336,TradingSessionID)
	msg.append_pair(340,TradSesStatus)
	if TradSesReqID != None:
		msg.append_pair(335,TradSesReqID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if TradSesMethod != None:
		msg.append_pair(338,TradSesMethod)
	if TradSesMode != None:
		msg.append_pair(339,TradSesMode)
	if UnsolicitedIndicator != None:
		msg.append_pair(325,UnsolicitedIndicator)
	if TradSesStatusRejReason != None:
		msg.append_pair(567,TradSesStatusRejReason)
	if TradSesStartTime != None:
		msg.append_pair(341,TradSesStartTime)
	if TradSesOpenTime != None:
		msg.append_pair(342,TradSesOpenTime)
	if TradSesPreCloseTime != None:
		msg.append_pair(343,TradSesPreCloseTime)
	if TradSesCloseTime != None:
		msg.append_pair(344,TradSesCloseTime)
	if TradSesEndTime != None:
		msg.append_pair(345,TradSesEndTime)
	if TotalVolumeTraded != None:
		msg.append_pair(387,TotalVolumeTraded)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def MassQuote(MsgSeqNum,TargetCompID,QuoteID,QuotSetGrp,QuoteReqID=None,QuoteType=None,QuoteResponseLevel=None,Account=None,AcctIDSource=None,AccountType=None,DefBidSize=None,DefOfferSize=None,Parties=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,i,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(117,QuoteID)
	for tv in QuotSetGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if QuoteReqID != None:
		msg.append_pair(131,QuoteReqID)
	if QuoteType != None:
		msg.append_pair(537,QuoteType)
	if QuoteResponseLevel != None:
		msg.append_pair(301,QuoteResponseLevel)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if DefBidSize != None:
		msg.append_pair(293,DefBidSize)
	if DefOfferSize != None:
		msg.append_pair(294,DefOfferSize)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def BusinessMessageReject(MsgSeqNum,TargetCompID,RefMsgType,BusinessRejectReason,RefSeqNum=None,BusinessRejectRefID=None,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,j,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(372,RefMsgType)
	msg.append_pair(380,BusinessRejectReason)
	if RefSeqNum != None:
		msg.append_pair(45,RefSeqNum)
	if BusinessRejectRefID != None:
		msg.append_pair(379,BusinessRejectRefID)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def BidRequest(MsgSeqNum,TargetCompID,ClientBidID,BidRequestTransType,TotNoRelatedSym,BidType,BidTradeType,BasisPxType,BidID=None,ListName=None,NumTickets=None,Currency=None,SideValue1=None,SideValue2=None,LiquidityIndType=None,WtAverageLiquidity=None,ExchangeForPhysical=None,OutMainCntryUIndex=None,CrossPercent=None,ProgRptReqs=None,ProgPeriodInterval=None,IncTaxInd=None,ForexReq=None,NumBidders=None,TradeDate=None,StrikeTime=None,Text=None,EncodedTextLen=None,EncodedText=None,BidDescReqGrp=None,BidCompReqGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,k,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(391,ClientBidID)
	msg.append_pair(374,BidRequestTransType)
	msg.append_pair(393,TotNoRelatedSym)
	msg.append_pair(394,BidType)
	msg.append_pair(418,BidTradeType)
	msg.append_pair(419,BasisPxType)
	if BidID != None:
		msg.append_pair(390,BidID)
	if ListName != None:
		msg.append_pair(392,ListName)
	if NumTickets != None:
		msg.append_pair(395,NumTickets)
	if Currency != None:
		msg.append_pair(15,Currency)
	if SideValue1 != None:
		msg.append_pair(396,SideValue1)
	if SideValue2 != None:
		msg.append_pair(397,SideValue2)
	if LiquidityIndType != None:
		msg.append_pair(409,LiquidityIndType)
	if WtAverageLiquidity != None:
		msg.append_pair(410,WtAverageLiquidity)
	if ExchangeForPhysical != None:
		msg.append_pair(411,ExchangeForPhysical)
	if OutMainCntryUIndex != None:
		msg.append_pair(412,OutMainCntryUIndex)
	if CrossPercent != None:
		msg.append_pair(413,CrossPercent)
	if ProgRptReqs != None:
		msg.append_pair(414,ProgRptReqs)
	if ProgPeriodInterval != None:
		msg.append_pair(415,ProgPeriodInterval)
	if IncTaxInd != None:
		msg.append_pair(416,IncTaxInd)
	if ForexReq != None:
		msg.append_pair(121,ForexReq)
	if NumBidders != None:
		msg.append_pair(417,NumBidders)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if StrikeTime != None:
		msg.append_pair(443,StrikeTime)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if BidDescReqGrp != None:
		for tv in BidDescReqGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if BidCompReqGrp != None:
		for tv in BidCompReqGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def BidResponse(MsgSeqNum,TargetCompID,BidCompRspGrp,BidID=None,ClientBidID=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,l,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	for tv in BidCompRspGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if BidID != None:
		msg.append_pair(390,BidID)
	if ClientBidID != None:
		msg.append_pair(391,ClientBidID)
	return msg.encode()

def ListStrikePrice(MsgSeqNum,TargetCompID,ListID,TotNoStrikes,InstrmtStrkPxGrp,LastFragment=None,UndInstrmtStrkPxGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,m,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(66,ListID)
	msg.append_pair(422,TotNoStrikes)
	for tv in InstrmtStrkPxGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if LastFragment != None:
		msg.append_pair(893,LastFragment)
	if UndInstrmtStrkPxGrp != None:
		for tv in UndInstrmtStrkPxGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def XMLnonFIX(MsgSeqNum,TargetCompID,):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,n,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	return msg.encode()

def RegistrationInstructions(MsgSeqNum,TargetCompID,RegistID,RegistTransType,RegistRefID,ClOrdID=None,Account=None,AcctIDSource=None,RegistAcctType=None,TaxAdvantageType=None,OwnershipType=None,Parties=None,RgstDtlsGrp=None,RgstDistInstGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,o,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(513,RegistID)
	msg.append_pair(514,RegistTransType)
	msg.append_pair(508,RegistRefID)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if RegistAcctType != None:
		msg.append_pair(493,RegistAcctType)
	if TaxAdvantageType != None:
		msg.append_pair(495,TaxAdvantageType)
	if OwnershipType != None:
		msg.append_pair(517,OwnershipType)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if RgstDtlsGrp != None:
		for tv in RgstDtlsGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if RgstDistInstGrp != None:
		for tv in RgstDistInstGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def RegistrationInstructionsResponse(MsgSeqNum,TargetCompID,RegistID,RegistTransType,RegistRefID,RegistStatus,ClOrdID=None,Account=None,AcctIDSource=None,RegistRejReasonCode=None,RegistRejReasonText=None,Parties=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,p,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(513,RegistID)
	msg.append_pair(514,RegistTransType)
	msg.append_pair(508,RegistRefID)
	msg.append_pair(506,RegistStatus)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if RegistRejReasonCode != None:
		msg.append_pair(507,RegistRejReasonCode)
	if RegistRejReasonText != None:
		msg.append_pair(496,RegistRejReasonText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def OrderMassCancelRequest(MsgSeqNum,TargetCompID,ClOrdID,MassCancelRequestType,TransactTime,SecondaryClOrdID=None,TradingSessionID=None,TradingSessionSubID=None,Side=None,Text=None,EncodedTextLen=None,EncodedText=None,Instrument=None,UnderlyingInstrument=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,q,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(11,ClOrdID)
	msg.append_pair(530,MassCancelRequestType)
	msg.append_pair(60,TransactTime)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if Side != None:
		msg.append_pair(54,Side)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UnderlyingInstrument != None:
		for tv in UnderlyingInstrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def OrderMassCancelReport(MsgSeqNum,TargetCompID,OrderID,MassCancelRequestType,MassCancelResponse,ClOrdID=None,SecondaryClOrdID=None,SecondaryOrderID=None,MassCancelRejectReason=None,TotalAffectedOrders=None,TradingSessionID=None,TradingSessionSubID=None,Side=None,TransactTime=None,Text=None,EncodedTextLen=None,EncodedText=None,AffectedOrdGrp=None,Instrument=None,UnderlyingInstrument=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,r,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(37,OrderID)
	msg.append_pair(530,MassCancelRequestType)
	msg.append_pair(531,MassCancelResponse)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if MassCancelRejectReason != None:
		msg.append_pair(532,MassCancelRejectReason)
	if TotalAffectedOrders != None:
		msg.append_pair(533,TotalAffectedOrders)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if Side != None:
		msg.append_pair(54,Side)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if AffectedOrdGrp != None:
		for tv in AffectedOrdGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UnderlyingInstrument != None:
		for tv in UnderlyingInstrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def NewOrderCross(MsgSeqNum,TargetCompID,CrossID,CrossType,CrossPrioritization,TransactTime,OrdType,SideCrossOrdModGrp,Instrument,SettlType=None,SettlDate=None,HandlInst=None,ExecInst=None,MinQty=None,MaxFloor=None,ExDestination=None,ProcessCode=None,PrevClosePx=None,LocateReqd=None,PriceType=None,Price=None,StopPx=None,Currency=None,ComplianceID=None,IOIID=None,QuoteID=None,TimeInForce=None,EffectiveTime=None,ExpireDate=None,ExpireTime=None,GTBookingInst=None,MaxShow=None,TargetStrategy=None,TargetStrategyParameters=None,ParticipationRate=None,CancellationRights=None,MoneyLaunderingStatus=None,RegistID=None,Designation=None,UndInstrmtGrp=None,InstrmtLegGrp=None,TrdgSesGrp=None,Stipulations=None,SpreadOrBenchmarkCurveData=None,YieldData=None,PegInstructions=None,DiscretionInstructions=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,s,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(548,CrossID)
	msg.append_pair(549,CrossType)
	msg.append_pair(550,CrossPrioritization)
	msg.append_pair(60,TransactTime)
	msg.append_pair(40,OrdType)
	for tv in SideCrossOrdModGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if HandlInst != None:
		msg.append_pair(21,HandlInst)
	if ExecInst != None:
		msg.append_pair(18,ExecInst)
	if MinQty != None:
		msg.append_pair(110,MinQty)
	if MaxFloor != None:
		msg.append_pair(111,MaxFloor)
	if ExDestination != None:
		msg.append_pair(100,ExDestination)
	if ProcessCode != None:
		msg.append_pair(81,ProcessCode)
	if PrevClosePx != None:
		msg.append_pair(140,PrevClosePx)
	if LocateReqd != None:
		msg.append_pair(114,LocateReqd)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if Price != None:
		msg.append_pair(44,Price)
	if StopPx != None:
		msg.append_pair(99,StopPx)
	if Currency != None:
		msg.append_pair(15,Currency)
	if ComplianceID != None:
		msg.append_pair(376,ComplianceID)
	if IOIID != None:
		msg.append_pair(23,IOIID)
	if QuoteID != None:
		msg.append_pair(117,QuoteID)
	if TimeInForce != None:
		msg.append_pair(59,TimeInForce)
	if EffectiveTime != None:
		msg.append_pair(168,EffectiveTime)
	if ExpireDate != None:
		msg.append_pair(432,ExpireDate)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if GTBookingInst != None:
		msg.append_pair(427,GTBookingInst)
	if MaxShow != None:
		msg.append_pair(210,MaxShow)
	if TargetStrategy != None:
		msg.append_pair(847,TargetStrategy)
	if TargetStrategyParameters != None:
		msg.append_pair(848,TargetStrategyParameters)
	if ParticipationRate != None:
		msg.append_pair(849,ParticipationRate)
	if CancellationRights != None:
		msg.append_pair(480,CancellationRights)
	if MoneyLaunderingStatus != None:
		msg.append_pair(481,MoneyLaunderingStatus)
	if RegistID != None:
		msg.append_pair(513,RegistID)
	if Designation != None:
		msg.append_pair(494,Designation)
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PegInstructions != None:
		for tv in PegInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if DiscretionInstructions != None:
		for tv in DiscretionInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def CrossOrderCancelReplaceRequest(MsgSeqNum,TargetCompID,CrossID,OrigCrossID,CrossType,CrossPrioritization,TransactTime,OrdType,SideCrossOrdModGrp,Instrument,OrderID=None,SettlType=None,SettlDate=None,HandlInst=None,ExecInst=None,MinQty=None,MaxFloor=None,ExDestination=None,ProcessCode=None,PrevClosePx=None,LocateReqd=None,PriceType=None,Price=None,StopPx=None,Currency=None,ComplianceID=None,IOIID=None,QuoteID=None,TimeInForce=None,EffectiveTime=None,ExpireDate=None,ExpireTime=None,GTBookingInst=None,MaxShow=None,TargetStrategy=None,TargetStrategyParameters=None,ParticipationRate=None,CancellationRights=None,MoneyLaunderingStatus=None,RegistID=None,Designation=None,UndInstrmtGrp=None,InstrmtLegGrp=None,TrdgSesGrp=None,Stipulations=None,SpreadOrBenchmarkCurveData=None,YieldData=None,PegInstructions=None,DiscretionInstructions=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,t,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(548,CrossID)
	msg.append_pair(551,OrigCrossID)
	msg.append_pair(549,CrossType)
	msg.append_pair(550,CrossPrioritization)
	msg.append_pair(60,TransactTime)
	msg.append_pair(40,OrdType)
	for tv in SideCrossOrdModGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if HandlInst != None:
		msg.append_pair(21,HandlInst)
	if ExecInst != None:
		msg.append_pair(18,ExecInst)
	if MinQty != None:
		msg.append_pair(110,MinQty)
	if MaxFloor != None:
		msg.append_pair(111,MaxFloor)
	if ExDestination != None:
		msg.append_pair(100,ExDestination)
	if ProcessCode != None:
		msg.append_pair(81,ProcessCode)
	if PrevClosePx != None:
		msg.append_pair(140,PrevClosePx)
	if LocateReqd != None:
		msg.append_pair(114,LocateReqd)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if Price != None:
		msg.append_pair(44,Price)
	if StopPx != None:
		msg.append_pair(99,StopPx)
	if Currency != None:
		msg.append_pair(15,Currency)
	if ComplianceID != None:
		msg.append_pair(376,ComplianceID)
	if IOIID != None:
		msg.append_pair(23,IOIID)
	if QuoteID != None:
		msg.append_pair(117,QuoteID)
	if TimeInForce != None:
		msg.append_pair(59,TimeInForce)
	if EffectiveTime != None:
		msg.append_pair(168,EffectiveTime)
	if ExpireDate != None:
		msg.append_pair(432,ExpireDate)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if GTBookingInst != None:
		msg.append_pair(427,GTBookingInst)
	if MaxShow != None:
		msg.append_pair(210,MaxShow)
	if TargetStrategy != None:
		msg.append_pair(847,TargetStrategy)
	if TargetStrategyParameters != None:
		msg.append_pair(848,TargetStrategyParameters)
	if ParticipationRate != None:
		msg.append_pair(849,ParticipationRate)
	if CancellationRights != None:
		msg.append_pair(480,CancellationRights)
	if MoneyLaunderingStatus != None:
		msg.append_pair(481,MoneyLaunderingStatus)
	if RegistID != None:
		msg.append_pair(513,RegistID)
	if Designation != None:
		msg.append_pair(494,Designation)
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PegInstructions != None:
		for tv in PegInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if DiscretionInstructions != None:
		for tv in DiscretionInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def CrossOrderCancelRequest(MsgSeqNum,TargetCompID,CrossID,OrigCrossID,CrossType,CrossPrioritization,TransactTime,SideCrossOrdCxlGrp,Instrument,OrderID=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,u,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(548,CrossID)
	msg.append_pair(551,OrigCrossID)
	msg.append_pair(549,CrossType)
	msg.append_pair(550,CrossPrioritization)
	msg.append_pair(60,TransactTime)
	for tv in SideCrossOrdCxlGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def SecurityTypeRequest(MsgSeqNum,TargetCompID,SecurityReqID,Text=None,EncodedTextLen=None,EncodedText=None,TradingSessionID=None,TradingSessionSubID=None,Product=None,SecurityType=None,SecuritySubType=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,v,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(320,SecurityReqID)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if Product != None:
		msg.append_pair(460,Product)
	if SecurityType != None:
		msg.append_pair(167,SecurityType)
	if SecuritySubType != None:
		msg.append_pair(762,SecuritySubType)
	return msg.encode()

def SecurityTypes(MsgSeqNum,TargetCompID,SecurityReqID,SecurityResponseID,SecurityResponseType,TotNoSecurityTypes=None,LastFragment=None,Text=None,EncodedTextLen=None,EncodedText=None,TradingSessionID=None,TradingSessionSubID=None,SubscriptionRequestType=None,SecTypesGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,w,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(320,SecurityReqID)
	msg.append_pair(322,SecurityResponseID)
	msg.append_pair(323,SecurityResponseType)
	if TotNoSecurityTypes != None:
		msg.append_pair(557,TotNoSecurityTypes)
	if LastFragment != None:
		msg.append_pair(893,LastFragment)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if SecTypesGrp != None:
		for tv in SecTypesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def SecurityListRequest(MsgSeqNum,TargetCompID,SecurityReqID,SecurityListRequestType,Currency=None,Text=None,EncodedTextLen=None,EncodedText=None,TradingSessionID=None,TradingSessionSubID=None,SubscriptionRequestType=None,Instrument=None,InstrumentExtension=None,FinancingDetails=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,x,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(320,SecurityReqID)
	msg.append_pair(559,SecurityListRequestType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrumentExtension != None:
		for tv in InstrumentExtension.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def SecurityList(MsgSeqNum,TargetCompID,SecurityReqID,SecurityResponseID,SecurityRequestResult,TotNoRelatedSym=None,LastFragment=None,SecListGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,y,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(320,SecurityReqID)
	msg.append_pair(322,SecurityResponseID)
	msg.append_pair(560,SecurityRequestResult)
	if TotNoRelatedSym != None:
		msg.append_pair(393,TotNoRelatedSym)
	if LastFragment != None:
		msg.append_pair(893,LastFragment)
	if SecListGrp != None:
		for tv in SecListGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def DerivativeSecurityListRequest(MsgSeqNum,TargetCompID,SecurityReqID,SecurityListRequestType,SecuritySubType=None,Currency=None,Text=None,EncodedTextLen=None,EncodedText=None,TradingSessionID=None,TradingSessionSubID=None,SubscriptionRequestType=None,UnderlyingInstrument=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,z,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(320,SecurityReqID)
	msg.append_pair(559,SecurityListRequestType)
	if SecuritySubType != None:
		msg.append_pair(762,SecuritySubType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if UnderlyingInstrument != None:
		for tv in UnderlyingInstrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def DerivativeSecurityList(MsgSeqNum,TargetCompID,SecurityReqID,SecurityResponseID,SecurityRequestResult,TotNoRelatedSym=None,LastFragment=None,UnderlyingInstrument=None,RelSymDerivSecGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AA,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(320,SecurityReqID)
	msg.append_pair(322,SecurityResponseID)
	msg.append_pair(560,SecurityRequestResult)
	if TotNoRelatedSym != None:
		msg.append_pair(393,TotNoRelatedSym)
	if LastFragment != None:
		msg.append_pair(893,LastFragment)
	if UnderlyingInstrument != None:
		for tv in UnderlyingInstrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if RelSymDerivSecGrp != None:
		for tv in RelSymDerivSecGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def NewOrderMultileg(MsgSeqNum,TargetCompID,ClOrdID,Side,TransactTime,OrdType,Instrument,LegOrdGrp,OrderQtyData,SecondaryClOrdID=None,ClOrdLinkID=None,TradeOriginationDate=None,TradeDate=None,Account=None,AcctIDSource=None,AccountType=None,DayBookingInst=None,BookingUnit=None,PreallocMethod=None,AllocID=None,SettlType=None,SettlDate=None,CashMargin=None,ClearingFeeIndicator=None,HandlInst=None,ExecInst=None,MinQty=None,MaxFloor=None,ExDestination=None,ProcessCode=None,PrevClosePx=None,LocateReqd=None,QtyType=None,PriceType=None,Price=None,StopPx=None,Currency=None,ComplianceID=None,SolicitedFlag=None,IOIID=None,QuoteID=None,TimeInForce=None,EffectiveTime=None,ExpireDate=None,ExpireTime=None,GTBookingInst=None,OrderCapacity=None,OrderRestrictions=None,CustOrderCapacity=None,ForexReq=None,SettlCurrency=None,BookingType=None,Text=None,EncodedTextLen=None,EncodedText=None,PositionEffect=None,CoveredOrUncovered=None,MaxShow=None,TargetStrategy=None,TargetStrategyParameters=None,ParticipationRate=None,CancellationRights=None,MoneyLaunderingStatus=None,RegistID=None,Designation=None,MultiLegRptTypeReq=None,Parties=None,PreAllocMlegGrp=None,TrdgSesGrp=None,UndInstrmtGrp=None,CommissionData=None,PegInstructions=None,DiscretionInstructions=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AB,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(11,ClOrdID)
	msg.append_pair(54,Side)
	msg.append_pair(60,TransactTime)
	msg.append_pair(40,OrdType)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in LegOrdGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in OrderQtyData.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if ClOrdLinkID != None:
		msg.append_pair(583,ClOrdLinkID)
	if TradeOriginationDate != None:
		msg.append_pair(229,TradeOriginationDate)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if DayBookingInst != None:
		msg.append_pair(589,DayBookingInst)
	if BookingUnit != None:
		msg.append_pair(590,BookingUnit)
	if PreallocMethod != None:
		msg.append_pair(591,PreallocMethod)
	if AllocID != None:
		msg.append_pair(70,AllocID)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if CashMargin != None:
		msg.append_pair(544,CashMargin)
	if ClearingFeeIndicator != None:
		msg.append_pair(635,ClearingFeeIndicator)
	if HandlInst != None:
		msg.append_pair(21,HandlInst)
	if ExecInst != None:
		msg.append_pair(18,ExecInst)
	if MinQty != None:
		msg.append_pair(110,MinQty)
	if MaxFloor != None:
		msg.append_pair(111,MaxFloor)
	if ExDestination != None:
		msg.append_pair(100,ExDestination)
	if ProcessCode != None:
		msg.append_pair(81,ProcessCode)
	if PrevClosePx != None:
		msg.append_pair(140,PrevClosePx)
	if LocateReqd != None:
		msg.append_pair(114,LocateReqd)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if Price != None:
		msg.append_pair(44,Price)
	if StopPx != None:
		msg.append_pair(99,StopPx)
	if Currency != None:
		msg.append_pair(15,Currency)
	if ComplianceID != None:
		msg.append_pair(376,ComplianceID)
	if SolicitedFlag != None:
		msg.append_pair(377,SolicitedFlag)
	if IOIID != None:
		msg.append_pair(23,IOIID)
	if QuoteID != None:
		msg.append_pair(117,QuoteID)
	if TimeInForce != None:
		msg.append_pair(59,TimeInForce)
	if EffectiveTime != None:
		msg.append_pair(168,EffectiveTime)
	if ExpireDate != None:
		msg.append_pair(432,ExpireDate)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if GTBookingInst != None:
		msg.append_pair(427,GTBookingInst)
	if OrderCapacity != None:
		msg.append_pair(528,OrderCapacity)
	if OrderRestrictions != None:
		msg.append_pair(529,OrderRestrictions)
	if CustOrderCapacity != None:
		msg.append_pair(582,CustOrderCapacity)
	if ForexReq != None:
		msg.append_pair(121,ForexReq)
	if SettlCurrency != None:
		msg.append_pair(120,SettlCurrency)
	if BookingType != None:
		msg.append_pair(775,BookingType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if PositionEffect != None:
		msg.append_pair(77,PositionEffect)
	if CoveredOrUncovered != None:
		msg.append_pair(203,CoveredOrUncovered)
	if MaxShow != None:
		msg.append_pair(210,MaxShow)
	if TargetStrategy != None:
		msg.append_pair(847,TargetStrategy)
	if TargetStrategyParameters != None:
		msg.append_pair(848,TargetStrategyParameters)
	if ParticipationRate != None:
		msg.append_pair(849,ParticipationRate)
	if CancellationRights != None:
		msg.append_pair(480,CancellationRights)
	if MoneyLaunderingStatus != None:
		msg.append_pair(481,MoneyLaunderingStatus)
	if RegistID != None:
		msg.append_pair(513,RegistID)
	if Designation != None:
		msg.append_pair(494,Designation)
	if MultiLegRptTypeReq != None:
		msg.append_pair(563,MultiLegRptTypeReq)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PreAllocMlegGrp != None:
		for tv in PreAllocMlegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if CommissionData != None:
		for tv in CommissionData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PegInstructions != None:
		for tv in PegInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if DiscretionInstructions != None:
		for tv in DiscretionInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def MultilegOrderCancelReplace(MsgSeqNum,TargetCompID,OrigClOrdID,ClOrdID,Side,TransactTime,OrdType,Instrument,LegOrdGrp,OrderQtyData,OrderID=None,SecondaryClOrdID=None,ClOrdLinkID=None,OrigOrdModTime=None,TradeOriginationDate=None,TradeDate=None,Account=None,AcctIDSource=None,AccountType=None,DayBookingInst=None,BookingUnit=None,PreallocMethod=None,AllocID=None,SettlType=None,SettlDate=None,CashMargin=None,ClearingFeeIndicator=None,HandlInst=None,ExecInst=None,MinQty=None,MaxFloor=None,ExDestination=None,ProcessCode=None,PrevClosePx=None,LocateReqd=None,QtyType=None,PriceType=None,Price=None,StopPx=None,Currency=None,ComplianceID=None,SolicitedFlag=None,IOIID=None,QuoteID=None,TimeInForce=None,EffectiveTime=None,ExpireDate=None,ExpireTime=None,GTBookingInst=None,OrderCapacity=None,OrderRestrictions=None,CustOrderCapacity=None,ForexReq=None,SettlCurrency=None,BookingType=None,Text=None,EncodedTextLen=None,EncodedText=None,PositionEffect=None,CoveredOrUncovered=None,MaxShow=None,TargetStrategy=None,TargetStrategyParameters=None,ParticipationRate=None,CancellationRights=None,MoneyLaunderingStatus=None,RegistID=None,Designation=None,MultiLegRptTypeReq=None,Parties=None,PreAllocMlegGrp=None,TrdgSesGrp=None,UndInstrmtGrp=None,CommissionData=None,PegInstructions=None,DiscretionInstructions=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AC,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(41,OrigClOrdID)
	msg.append_pair(11,ClOrdID)
	msg.append_pair(54,Side)
	msg.append_pair(60,TransactTime)
	msg.append_pair(40,OrdType)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in LegOrdGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in OrderQtyData.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if ClOrdLinkID != None:
		msg.append_pair(583,ClOrdLinkID)
	if OrigOrdModTime != None:
		msg.append_pair(586,OrigOrdModTime)
	if TradeOriginationDate != None:
		msg.append_pair(229,TradeOriginationDate)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if DayBookingInst != None:
		msg.append_pair(589,DayBookingInst)
	if BookingUnit != None:
		msg.append_pair(590,BookingUnit)
	if PreallocMethod != None:
		msg.append_pair(591,PreallocMethod)
	if AllocID != None:
		msg.append_pair(70,AllocID)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if CashMargin != None:
		msg.append_pair(544,CashMargin)
	if ClearingFeeIndicator != None:
		msg.append_pair(635,ClearingFeeIndicator)
	if HandlInst != None:
		msg.append_pair(21,HandlInst)
	if ExecInst != None:
		msg.append_pair(18,ExecInst)
	if MinQty != None:
		msg.append_pair(110,MinQty)
	if MaxFloor != None:
		msg.append_pair(111,MaxFloor)
	if ExDestination != None:
		msg.append_pair(100,ExDestination)
	if ProcessCode != None:
		msg.append_pair(81,ProcessCode)
	if PrevClosePx != None:
		msg.append_pair(140,PrevClosePx)
	if LocateReqd != None:
		msg.append_pair(114,LocateReqd)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if Price != None:
		msg.append_pair(44,Price)
	if StopPx != None:
		msg.append_pair(99,StopPx)
	if Currency != None:
		msg.append_pair(15,Currency)
	if ComplianceID != None:
		msg.append_pair(376,ComplianceID)
	if SolicitedFlag != None:
		msg.append_pair(377,SolicitedFlag)
	if IOIID != None:
		msg.append_pair(23,IOIID)
	if QuoteID != None:
		msg.append_pair(117,QuoteID)
	if TimeInForce != None:
		msg.append_pair(59,TimeInForce)
	if EffectiveTime != None:
		msg.append_pair(168,EffectiveTime)
	if ExpireDate != None:
		msg.append_pair(432,ExpireDate)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if GTBookingInst != None:
		msg.append_pair(427,GTBookingInst)
	if OrderCapacity != None:
		msg.append_pair(528,OrderCapacity)
	if OrderRestrictions != None:
		msg.append_pair(529,OrderRestrictions)
	if CustOrderCapacity != None:
		msg.append_pair(582,CustOrderCapacity)
	if ForexReq != None:
		msg.append_pair(121,ForexReq)
	if SettlCurrency != None:
		msg.append_pair(120,SettlCurrency)
	if BookingType != None:
		msg.append_pair(775,BookingType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if PositionEffect != None:
		msg.append_pair(77,PositionEffect)
	if CoveredOrUncovered != None:
		msg.append_pair(203,CoveredOrUncovered)
	if MaxShow != None:
		msg.append_pair(210,MaxShow)
	if TargetStrategy != None:
		msg.append_pair(847,TargetStrategy)
	if TargetStrategyParameters != None:
		msg.append_pair(848,TargetStrategyParameters)
	if ParticipationRate != None:
		msg.append_pair(849,ParticipationRate)
	if CancellationRights != None:
		msg.append_pair(480,CancellationRights)
	if MoneyLaunderingStatus != None:
		msg.append_pair(481,MoneyLaunderingStatus)
	if RegistID != None:
		msg.append_pair(513,RegistID)
	if Designation != None:
		msg.append_pair(494,Designation)
	if MultiLegRptTypeReq != None:
		msg.append_pair(563,MultiLegRptTypeReq)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PreAllocMlegGrp != None:
		for tv in PreAllocMlegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if CommissionData != None:
		for tv in CommissionData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PegInstructions != None:
		for tv in PegInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if DiscretionInstructions != None:
		for tv in DiscretionInstructions.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def TradeCaptureReportRequest(MsgSeqNum,TargetCompID,TradeRequestID,TradeRequestType,SubscriptionRequestType=None,TradeReportID=None,SecondaryTradeReportID=None,ExecID=None,ExecType=None,OrderID=None,ClOrdID=None,MatchStatus=None,TrdType=None,TrdSubType=None,TransferReason=None,SecondaryTrdType=None,TradeLinkID=None,TrdMatchID=None,ClearingBusinessDate=None,TradingSessionID=None,TradingSessionSubID=None,TimeBracket=None,Side=None,MultiLegReportingType=None,TradeInputSource=None,TradeInputDevice=None,ResponseTransportType=None,ResponseDestination=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,Instrument=None,InstrumentExtension=None,FinancingDetails=None,UndInstrmtGrp=None,InstrmtLegGrp=None,TrdCapDtGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AD,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(568,TradeRequestID)
	msg.append_pair(569,TradeRequestType)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if TradeReportID != None:
		msg.append_pair(571,TradeReportID)
	if SecondaryTradeReportID != None:
		msg.append_pair(818,SecondaryTradeReportID)
	if ExecID != None:
		msg.append_pair(17,ExecID)
	if ExecType != None:
		msg.append_pair(150,ExecType)
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if MatchStatus != None:
		msg.append_pair(573,MatchStatus)
	if TrdType != None:
		msg.append_pair(828,TrdType)
	if TrdSubType != None:
		msg.append_pair(829,TrdSubType)
	if TransferReason != None:
		msg.append_pair(830,TransferReason)
	if SecondaryTrdType != None:
		msg.append_pair(855,SecondaryTrdType)
	if TradeLinkID != None:
		msg.append_pair(820,TradeLinkID)
	if TrdMatchID != None:
		msg.append_pair(880,TrdMatchID)
	if ClearingBusinessDate != None:
		msg.append_pair(715,ClearingBusinessDate)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if TimeBracket != None:
		msg.append_pair(943,TimeBracket)
	if Side != None:
		msg.append_pair(54,Side)
	if MultiLegReportingType != None:
		msg.append_pair(442,MultiLegReportingType)
	if TradeInputSource != None:
		msg.append_pair(578,TradeInputSource)
	if TradeInputDevice != None:
		msg.append_pair(579,TradeInputDevice)
	if ResponseTransportType != None:
		msg.append_pair(725,ResponseTransportType)
	if ResponseDestination != None:
		msg.append_pair(726,ResponseDestination)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrumentExtension != None:
		for tv in InstrumentExtension.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdCapDtGrp != None:
		for tv in TrdCapDtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def TradeCaptureReport(MsgSeqNum,TargetCompID,TradeReportID,PreviouslyReported,LastQty,LastPx,TradeDate,TransactTime,Instrument,TrdCapRptSideGrp,TradeReportTransType=None,TradeReportType=None,TradeRequestID=None,TrdType=None,TrdSubType=None,SecondaryTrdType=None,TransferReason=None,ExecType=None,TotNumTradeReports=None,LastRptRequested=None,UnsolicitedIndicator=None,SubscriptionRequestType=None,TradeReportRefID=None,SecondaryTradeReportRefID=None,SecondaryTradeReportID=None,TradeLinkID=None,TrdMatchID=None,ExecID=None,OrdStatus=None,SecondaryExecID=None,ExecRestatementReason=None,PriceType=None,QtyType=None,UnderlyingTradingSessionID=None,UnderlyingTradingSessionSubID=None,LastParPx=None,LastSpotRate=None,LastForwardPoints=None,LastMkt=None,ClearingBusinessDate=None,AvgPx=None,AvgPxIndicator=None,MultiLegReportingType=None,TradeLegRefID=None,SettlType=None,SettlDate=None,MatchStatus=None,MatchType=None,CopyMsgIndicator=None,PublishTrdIndicator=None,ShortSaleReason=None,FinancingDetails=None,OrderQtyData=None,YieldData=None,UndInstrmtGrp=None,SpreadOrBenchmarkCurveData=None,PositionAmountData=None,TrdInstrmtLegGrp=None,TrdRegTimestamps=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AE,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(571,TradeReportID)
	msg.append_pair(570,PreviouslyReported)
	msg.append_pair(32,LastQty)
	msg.append_pair(31,LastPx)
	msg.append_pair(75,TradeDate)
	msg.append_pair(60,TransactTime)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in TrdCapRptSideGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if TradeReportTransType != None:
		msg.append_pair(487,TradeReportTransType)
	if TradeReportType != None:
		msg.append_pair(856,TradeReportType)
	if TradeRequestID != None:
		msg.append_pair(568,TradeRequestID)
	if TrdType != None:
		msg.append_pair(828,TrdType)
	if TrdSubType != None:
		msg.append_pair(829,TrdSubType)
	if SecondaryTrdType != None:
		msg.append_pair(855,SecondaryTrdType)
	if TransferReason != None:
		msg.append_pair(830,TransferReason)
	if ExecType != None:
		msg.append_pair(150,ExecType)
	if TotNumTradeReports != None:
		msg.append_pair(748,TotNumTradeReports)
	if LastRptRequested != None:
		msg.append_pair(912,LastRptRequested)
	if UnsolicitedIndicator != None:
		msg.append_pair(325,UnsolicitedIndicator)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if TradeReportRefID != None:
		msg.append_pair(572,TradeReportRefID)
	if SecondaryTradeReportRefID != None:
		msg.append_pair(881,SecondaryTradeReportRefID)
	if SecondaryTradeReportID != None:
		msg.append_pair(818,SecondaryTradeReportID)
	if TradeLinkID != None:
		msg.append_pair(820,TradeLinkID)
	if TrdMatchID != None:
		msg.append_pair(880,TrdMatchID)
	if ExecID != None:
		msg.append_pair(17,ExecID)
	if OrdStatus != None:
		msg.append_pair(39,OrdStatus)
	if SecondaryExecID != None:
		msg.append_pair(527,SecondaryExecID)
	if ExecRestatementReason != None:
		msg.append_pair(378,ExecRestatementReason)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if UnderlyingTradingSessionID != None:
		msg.append_pair(822,UnderlyingTradingSessionID)
	if UnderlyingTradingSessionSubID != None:
		msg.append_pair(823,UnderlyingTradingSessionSubID)
	if LastParPx != None:
		msg.append_pair(669,LastParPx)
	if LastSpotRate != None:
		msg.append_pair(194,LastSpotRate)
	if LastForwardPoints != None:
		msg.append_pair(195,LastForwardPoints)
	if LastMkt != None:
		msg.append_pair(30,LastMkt)
	if ClearingBusinessDate != None:
		msg.append_pair(715,ClearingBusinessDate)
	if AvgPx != None:
		msg.append_pair(6,AvgPx)
	if AvgPxIndicator != None:
		msg.append_pair(819,AvgPxIndicator)
	if MultiLegReportingType != None:
		msg.append_pair(442,MultiLegReportingType)
	if TradeLegRefID != None:
		msg.append_pair(824,TradeLegRefID)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if MatchStatus != None:
		msg.append_pair(573,MatchStatus)
	if MatchType != None:
		msg.append_pair(574,MatchType)
	if CopyMsgIndicator != None:
		msg.append_pair(797,CopyMsgIndicator)
	if PublishTrdIndicator != None:
		msg.append_pair(852,PublishTrdIndicator)
	if ShortSaleReason != None:
		msg.append_pair(853,ShortSaleReason)
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if OrderQtyData != None:
		for tv in OrderQtyData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PositionAmountData != None:
		for tv in PositionAmountData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdInstrmtLegGrp != None:
		for tv in TrdInstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdRegTimestamps != None:
		for tv in TrdRegTimestamps.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def OrderMassStatusRequest(MsgSeqNum,TargetCompID,MassStatusReqID,MassStatusReqType,Account=None,AcctIDSource=None,TradingSessionID=None,TradingSessionSubID=None,Side=None,Parties=None,Instrument=None,UnderlyingInstrument=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AF,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(584,MassStatusReqID)
	msg.append_pair(585,MassStatusReqType)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if Side != None:
		msg.append_pair(54,Side)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UnderlyingInstrument != None:
		for tv in UnderlyingInstrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def QuoteRequestReject(MsgSeqNum,TargetCompID,QuoteReqID,QuoteRequestRejectReason,QuotReqRjctGrp,RFQReqID=None,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AG,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(131,QuoteReqID)
	msg.append_pair(658,QuoteRequestRejectReason)
	for tv in QuotReqRjctGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if RFQReqID != None:
		msg.append_pair(644,RFQReqID)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def RFQRequest(MsgSeqNum,TargetCompID,RFQReqID,RFQReqGrp,SubscriptionRequestType=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AH,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(644,RFQReqID)
	for tv in RFQReqGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	return msg.encode()

def QuoteStatusReport(MsgSeqNum,TargetCompID,QuoteID,Instrument,QuoteStatusReqID=None,QuoteReqID=None,QuoteRespID=None,QuoteType=None,TradingSessionID=None,TradingSessionSubID=None,Side=None,SettlType=None,SettlDate=None,SettlDate2=None,OrderQty2=None,Currency=None,Account=None,AcctIDSource=None,AccountType=None,ExpireTime=None,Price=None,PriceType=None,BidPx=None,OfferPx=None,MktBidPx=None,MktOfferPx=None,MinBidSize=None,BidSize=None,MinOfferSize=None,OfferSize=None,ValidUntilTime=None,BidSpotRate=None,OfferSpotRate=None,BidForwardPoints=None,OfferForwardPoints=None,MidPx=None,BidYield=None,MidYield=None,OfferYield=None,TransactTime=None,OrdType=None,BidForwardPoints2=None,OfferForwardPoints2=None,SettlCurrBidFxRate=None,SettlCurrOfferFxRate=None,SettlCurrFxRateCalc=None,CommType=None,Commission=None,CustOrderCapacity=None,ExDestination=None,QuoteStatus=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,FinancingDetails=None,UndInstrmtGrp=None,OrderQtyData=None,Stipulations=None,LegQuotStatGrp=None,QuotQualGrp=None,SpreadOrBenchmarkCurveData=None,YieldData=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AI,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(117,QuoteID)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if QuoteStatusReqID != None:
		msg.append_pair(649,QuoteStatusReqID)
	if QuoteReqID != None:
		msg.append_pair(131,QuoteReqID)
	if QuoteRespID != None:
		msg.append_pair(693,QuoteRespID)
	if QuoteType != None:
		msg.append_pair(537,QuoteType)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if Side != None:
		msg.append_pair(54,Side)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if SettlDate2 != None:
		msg.append_pair(193,SettlDate2)
	if OrderQty2 != None:
		msg.append_pair(192,OrderQty2)
	if Currency != None:
		msg.append_pair(15,Currency)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if Price != None:
		msg.append_pair(44,Price)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if BidPx != None:
		msg.append_pair(132,BidPx)
	if OfferPx != None:
		msg.append_pair(133,OfferPx)
	if MktBidPx != None:
		msg.append_pair(645,MktBidPx)
	if MktOfferPx != None:
		msg.append_pair(646,MktOfferPx)
	if MinBidSize != None:
		msg.append_pair(647,MinBidSize)
	if BidSize != None:
		msg.append_pair(134,BidSize)
	if MinOfferSize != None:
		msg.append_pair(648,MinOfferSize)
	if OfferSize != None:
		msg.append_pair(135,OfferSize)
	if ValidUntilTime != None:
		msg.append_pair(62,ValidUntilTime)
	if BidSpotRate != None:
		msg.append_pair(188,BidSpotRate)
	if OfferSpotRate != None:
		msg.append_pair(190,OfferSpotRate)
	if BidForwardPoints != None:
		msg.append_pair(189,BidForwardPoints)
	if OfferForwardPoints != None:
		msg.append_pair(191,OfferForwardPoints)
	if MidPx != None:
		msg.append_pair(631,MidPx)
	if BidYield != None:
		msg.append_pair(632,BidYield)
	if MidYield != None:
		msg.append_pair(633,MidYield)
	if OfferYield != None:
		msg.append_pair(634,OfferYield)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if OrdType != None:
		msg.append_pair(40,OrdType)
	if BidForwardPoints2 != None:
		msg.append_pair(642,BidForwardPoints2)
	if OfferForwardPoints2 != None:
		msg.append_pair(643,OfferForwardPoints2)
	if SettlCurrBidFxRate != None:
		msg.append_pair(656,SettlCurrBidFxRate)
	if SettlCurrOfferFxRate != None:
		msg.append_pair(657,SettlCurrOfferFxRate)
	if SettlCurrFxRateCalc != None:
		msg.append_pair(156,SettlCurrFxRateCalc)
	if CommType != None:
		msg.append_pair(13,CommType)
	if Commission != None:
		msg.append_pair(12,Commission)
	if CustOrderCapacity != None:
		msg.append_pair(582,CustOrderCapacity)
	if ExDestination != None:
		msg.append_pair(100,ExDestination)
	if QuoteStatus != None:
		msg.append_pair(297,QuoteStatus)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if OrderQtyData != None:
		for tv in OrderQtyData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if LegQuotStatGrp != None:
		for tv in LegQuotStatGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if QuotQualGrp != None:
		for tv in QuotQualGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def QuoteResponse(MsgSeqNum,TargetCompID,QuoteRespID,QuoteRespType,Instrument,QuoteID=None,ClOrdID=None,OrderCapacity=None,IOIID=None,QuoteType=None,TradingSessionID=None,TradingSessionSubID=None,Side=None,SettlType=None,SettlDate=None,SettlDate2=None,OrderQty2=None,Currency=None,Account=None,AcctIDSource=None,AccountType=None,BidPx=None,OfferPx=None,MktBidPx=None,MktOfferPx=None,MinBidSize=None,BidSize=None,MinOfferSize=None,OfferSize=None,ValidUntilTime=None,BidSpotRate=None,OfferSpotRate=None,BidForwardPoints=None,OfferForwardPoints=None,MidPx=None,BidYield=None,MidYield=None,OfferYield=None,TransactTime=None,OrdType=None,BidForwardPoints2=None,OfferForwardPoints2=None,SettlCurrBidFxRate=None,SettlCurrOfferFxRate=None,SettlCurrFxRateCalc=None,Commission=None,CommType=None,CustOrderCapacity=None,ExDestination=None,Text=None,EncodedTextLen=None,EncodedText=None,Price=None,PriceType=None,QuotQualGrp=None,Parties=None,FinancingDetails=None,UndInstrmtGrp=None,OrderQtyData=None,Stipulations=None,LegQuotGrp=None,SpreadOrBenchmarkCurveData=None,YieldData=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AJ,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(693,QuoteRespID)
	msg.append_pair(694,QuoteRespType)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if QuoteID != None:
		msg.append_pair(117,QuoteID)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if OrderCapacity != None:
		msg.append_pair(528,OrderCapacity)
	if IOIID != None:
		msg.append_pair(23,IOIID)
	if QuoteType != None:
		msg.append_pair(537,QuoteType)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if Side != None:
		msg.append_pair(54,Side)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if SettlDate2 != None:
		msg.append_pair(193,SettlDate2)
	if OrderQty2 != None:
		msg.append_pair(192,OrderQty2)
	if Currency != None:
		msg.append_pair(15,Currency)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if BidPx != None:
		msg.append_pair(132,BidPx)
	if OfferPx != None:
		msg.append_pair(133,OfferPx)
	if MktBidPx != None:
		msg.append_pair(645,MktBidPx)
	if MktOfferPx != None:
		msg.append_pair(646,MktOfferPx)
	if MinBidSize != None:
		msg.append_pair(647,MinBidSize)
	if BidSize != None:
		msg.append_pair(134,BidSize)
	if MinOfferSize != None:
		msg.append_pair(648,MinOfferSize)
	if OfferSize != None:
		msg.append_pair(135,OfferSize)
	if ValidUntilTime != None:
		msg.append_pair(62,ValidUntilTime)
	if BidSpotRate != None:
		msg.append_pair(188,BidSpotRate)
	if OfferSpotRate != None:
		msg.append_pair(190,OfferSpotRate)
	if BidForwardPoints != None:
		msg.append_pair(189,BidForwardPoints)
	if OfferForwardPoints != None:
		msg.append_pair(191,OfferForwardPoints)
	if MidPx != None:
		msg.append_pair(631,MidPx)
	if BidYield != None:
		msg.append_pair(632,BidYield)
	if MidYield != None:
		msg.append_pair(633,MidYield)
	if OfferYield != None:
		msg.append_pair(634,OfferYield)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if OrdType != None:
		msg.append_pair(40,OrdType)
	if BidForwardPoints2 != None:
		msg.append_pair(642,BidForwardPoints2)
	if OfferForwardPoints2 != None:
		msg.append_pair(643,OfferForwardPoints2)
	if SettlCurrBidFxRate != None:
		msg.append_pair(656,SettlCurrBidFxRate)
	if SettlCurrOfferFxRate != None:
		msg.append_pair(657,SettlCurrOfferFxRate)
	if SettlCurrFxRateCalc != None:
		msg.append_pair(156,SettlCurrFxRateCalc)
	if Commission != None:
		msg.append_pair(12,Commission)
	if CommType != None:
		msg.append_pair(13,CommType)
	if CustOrderCapacity != None:
		msg.append_pair(582,CustOrderCapacity)
	if ExDestination != None:
		msg.append_pair(100,ExDestination)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Price != None:
		msg.append_pair(44,Price)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if QuotQualGrp != None:
		for tv in QuotQualGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if OrderQtyData != None:
		for tv in OrderQtyData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if LegQuotGrp != None:
		for tv in LegQuotGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def Confirmation(MsgSeqNum,TargetCompID,ConfirmID,ConfirmTransType,ConfirmType,ConfirmStatus,TransactTime,TradeDate,AllocQty,Side,AllocAccount,AvgPx,GrossTradeAmt,NetMoney,Instrument,UndInstrmtGrp,InstrmtLegGrp,CpctyConfGrp,ConfirmRefID=None,ConfirmReqID=None,CopyMsgIndicator=None,LegalConfirm=None,AllocID=None,SecondaryAllocID=None,IndividualAllocID=None,QtyType=None,Currency=None,LastMkt=None,AllocAcctIDSource=None,AllocAccountType=None,AvgPxPrecision=None,PriceType=None,AvgParPx=None,ReportedPx=None,Text=None,EncodedTextLen=None,EncodedText=None,ProcessCode=None,NumDaysInterest=None,ExDate=None,AccruedInterestRate=None,AccruedInterestAmt=None,InterestAtMaturity=None,EndAccruedInterestAmt=None,StartCash=None,EndCash=None,Concession=None,TotalTakedown=None,MaturityNetMoney=None,SettlCurrAmt=None,SettlCurrency=None,SettlCurrFxRate=None,SettlCurrFxRateCalc=None,SettlType=None,SettlDate=None,SharedCommission=None,Parties=None,OrdAllocGrp=None,TrdRegTimestamps=None,InstrumentExtension=None,FinancingDetails=None,YieldData=None,SpreadOrBenchmarkCurveData=None,SettlInstructionsData=None,CommissionData=None,Stipulations=None,MiscFeesGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AK,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(664,ConfirmID)
	msg.append_pair(666,ConfirmTransType)
	msg.append_pair(773,ConfirmType)
	msg.append_pair(665,ConfirmStatus)
	msg.append_pair(60,TransactTime)
	msg.append_pair(75,TradeDate)
	msg.append_pair(80,AllocQty)
	msg.append_pair(54,Side)
	msg.append_pair(79,AllocAccount)
	msg.append_pair(6,AvgPx)
	msg.append_pair(381,GrossTradeAmt)
	msg.append_pair(118,NetMoney)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in UndInstrmtGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in InstrmtLegGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in CpctyConfGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if ConfirmRefID != None:
		msg.append_pair(772,ConfirmRefID)
	if ConfirmReqID != None:
		msg.append_pair(859,ConfirmReqID)
	if CopyMsgIndicator != None:
		msg.append_pair(797,CopyMsgIndicator)
	if LegalConfirm != None:
		msg.append_pair(650,LegalConfirm)
	if AllocID != None:
		msg.append_pair(70,AllocID)
	if SecondaryAllocID != None:
		msg.append_pair(793,SecondaryAllocID)
	if IndividualAllocID != None:
		msg.append_pair(467,IndividualAllocID)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if LastMkt != None:
		msg.append_pair(30,LastMkt)
	if AllocAcctIDSource != None:
		msg.append_pair(661,AllocAcctIDSource)
	if AllocAccountType != None:
		msg.append_pair(798,AllocAccountType)
	if AvgPxPrecision != None:
		msg.append_pair(74,AvgPxPrecision)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if AvgParPx != None:
		msg.append_pair(860,AvgParPx)
	if ReportedPx != None:
		msg.append_pair(861,ReportedPx)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if ProcessCode != None:
		msg.append_pair(81,ProcessCode)
	if NumDaysInterest != None:
		msg.append_pair(157,NumDaysInterest)
	if ExDate != None:
		msg.append_pair(230,ExDate)
	if AccruedInterestRate != None:
		msg.append_pair(158,AccruedInterestRate)
	if AccruedInterestAmt != None:
		msg.append_pair(159,AccruedInterestAmt)
	if InterestAtMaturity != None:
		msg.append_pair(738,InterestAtMaturity)
	if EndAccruedInterestAmt != None:
		msg.append_pair(920,EndAccruedInterestAmt)
	if StartCash != None:
		msg.append_pair(921,StartCash)
	if EndCash != None:
		msg.append_pair(922,EndCash)
	if Concession != None:
		msg.append_pair(238,Concession)
	if TotalTakedown != None:
		msg.append_pair(237,TotalTakedown)
	if MaturityNetMoney != None:
		msg.append_pair(890,MaturityNetMoney)
	if SettlCurrAmt != None:
		msg.append_pair(119,SettlCurrAmt)
	if SettlCurrency != None:
		msg.append_pair(120,SettlCurrency)
	if SettlCurrFxRate != None:
		msg.append_pair(155,SettlCurrFxRate)
	if SettlCurrFxRateCalc != None:
		msg.append_pair(156,SettlCurrFxRateCalc)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if SharedCommission != None:
		msg.append_pair(858,SharedCommission)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if OrdAllocGrp != None:
		for tv in OrdAllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdRegTimestamps != None:
		for tv in TrdRegTimestamps.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrumentExtension != None:
		for tv in InstrumentExtension.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SettlInstructionsData != None:
		for tv in SettlInstructionsData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if CommissionData != None:
		for tv in CommissionData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if MiscFeesGrp != None:
		for tv in MiscFeesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def PositionMaintenanceRequest(MsgSeqNum,TargetCompID,PosReqID,PosTransType,PosMaintAction,ClearingBusinessDate,Account,AccountType,TransactTime,Parties,Instrument,PositionQty,OrigPosReqRefID=None,PosMaintRptRefID=None,SettlSessID=None,SettlSessSubID=None,AcctIDSource=None,Currency=None,AdjustmentType=None,ContraryInstructionIndicator=None,PriorSpreadIndicator=None,ThresholdAmount=None,Text=None,EncodedTextLen=None,EncodedText=None,InstrmtLegGrp=None,UndInstrmtGrp=None,TrdgSesGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AL,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(710,PosReqID)
	msg.append_pair(709,PosTransType)
	msg.append_pair(712,PosMaintAction)
	msg.append_pair(715,ClearingBusinessDate)
	msg.append_pair(1,Account)
	msg.append_pair(581,AccountType)
	msg.append_pair(60,TransactTime)
	for tv in Parties.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in PositionQty.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if OrigPosReqRefID != None:
		msg.append_pair(713,OrigPosReqRefID)
	if PosMaintRptRefID != None:
		msg.append_pair(714,PosMaintRptRefID)
	if SettlSessID != None:
		msg.append_pair(716,SettlSessID)
	if SettlSessSubID != None:
		msg.append_pair(717,SettlSessSubID)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if Currency != None:
		msg.append_pair(15,Currency)
	if AdjustmentType != None:
		msg.append_pair(718,AdjustmentType)
	if ContraryInstructionIndicator != None:
		msg.append_pair(719,ContraryInstructionIndicator)
	if PriorSpreadIndicator != None:
		msg.append_pair(720,PriorSpreadIndicator)
	if ThresholdAmount != None:
		msg.append_pair(834,ThresholdAmount)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def PositionMaintenanceReport(MsgSeqNum,TargetCompID,PosMaintRptID,PosTransType,PosMaintAction,OrigPosReqRefID,PosMaintStatus,ClearingBusinessDate,Account,AccountType,TransactTime,Instrument,PositionQty,PositionAmountData,PosReqID=None,PosMaintResult=None,SettlSessID=None,SettlSessSubID=None,AcctIDSource=None,Currency=None,AdjustmentType=None,ThresholdAmount=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,InstrmtLegGrp=None,UndInstrmtGrp=None,TrdgSesGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AM,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(721,PosMaintRptID)
	msg.append_pair(709,PosTransType)
	msg.append_pair(712,PosMaintAction)
	msg.append_pair(713,OrigPosReqRefID)
	msg.append_pair(722,PosMaintStatus)
	msg.append_pair(715,ClearingBusinessDate)
	msg.append_pair(1,Account)
	msg.append_pair(581,AccountType)
	msg.append_pair(60,TransactTime)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in PositionQty.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in PositionAmountData.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if PosReqID != None:
		msg.append_pair(710,PosReqID)
	if PosMaintResult != None:
		msg.append_pair(723,PosMaintResult)
	if SettlSessID != None:
		msg.append_pair(716,SettlSessID)
	if SettlSessSubID != None:
		msg.append_pair(717,SettlSessSubID)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if Currency != None:
		msg.append_pair(15,Currency)
	if AdjustmentType != None:
		msg.append_pair(718,AdjustmentType)
	if ThresholdAmount != None:
		msg.append_pair(834,ThresholdAmount)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def RequestForPositions(MsgSeqNum,TargetCompID,PosReqID,PosReqType,Account,AccountType,ClearingBusinessDate,TransactTime,Parties,MatchStatus=None,SubscriptionRequestType=None,AcctIDSource=None,Currency=None,SettlSessID=None,SettlSessSubID=None,ResponseTransportType=None,ResponseDestination=None,Text=None,EncodedTextLen=None,EncodedText=None,Instrument=None,InstrmtLegGrp=None,UndInstrmtGrp=None,TrdgSesGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AN,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(710,PosReqID)
	msg.append_pair(724,PosReqType)
	msg.append_pair(1,Account)
	msg.append_pair(581,AccountType)
	msg.append_pair(715,ClearingBusinessDate)
	msg.append_pair(60,TransactTime)
	for tv in Parties.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if MatchStatus != None:
		msg.append_pair(573,MatchStatus)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if Currency != None:
		msg.append_pair(15,Currency)
	if SettlSessID != None:
		msg.append_pair(716,SettlSessID)
	if SettlSessSubID != None:
		msg.append_pair(717,SettlSessSubID)
	if ResponseTransportType != None:
		msg.append_pair(725,ResponseTransportType)
	if ResponseDestination != None:
		msg.append_pair(726,ResponseDestination)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdgSesGrp != None:
		for tv in TrdgSesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def RequestForPositionsAck(MsgSeqNum,TargetCompID,PosMaintRptID,PosReqResult,PosReqStatus,Account,AccountType,Parties,PosReqID=None,TotalNumPosReports=None,UnsolicitedIndicator=None,AcctIDSource=None,Currency=None,ResponseTransportType=None,ResponseDestination=None,Text=None,EncodedTextLen=None,EncodedText=None,Instrument=None,InstrmtLegGrp=None,UndInstrmtGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AO,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(721,PosMaintRptID)
	msg.append_pair(728,PosReqResult)
	msg.append_pair(729,PosReqStatus)
	msg.append_pair(1,Account)
	msg.append_pair(581,AccountType)
	for tv in Parties.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if PosReqID != None:
		msg.append_pair(710,PosReqID)
	if TotalNumPosReports != None:
		msg.append_pair(727,TotalNumPosReports)
	if UnsolicitedIndicator != None:
		msg.append_pair(325,UnsolicitedIndicator)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if Currency != None:
		msg.append_pair(15,Currency)
	if ResponseTransportType != None:
		msg.append_pair(725,ResponseTransportType)
	if ResponseDestination != None:
		msg.append_pair(726,ResponseDestination)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def PositionReport(MsgSeqNum,TargetCompID,PosMaintRptID,PosReqResult,ClearingBusinessDate,Account,AccountType,SettlPrice,SettlPriceType,PriorSettlPrice,Parties,PositionQty,PositionAmountData,PosReqID=None,PosReqType=None,SubscriptionRequestType=None,TotalNumPosReports=None,UnsolicitedIndicator=None,SettlSessID=None,SettlSessSubID=None,AcctIDSource=None,Currency=None,RegistStatus=None,DeliveryDate=None,Text=None,EncodedTextLen=None,EncodedText=None,Instrument=None,InstrmtLegGrp=None,PosUndInstrmtGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AP,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(721,PosMaintRptID)
	msg.append_pair(728,PosReqResult)
	msg.append_pair(715,ClearingBusinessDate)
	msg.append_pair(1,Account)
	msg.append_pair(581,AccountType)
	msg.append_pair(730,SettlPrice)
	msg.append_pair(731,SettlPriceType)
	msg.append_pair(734,PriorSettlPrice)
	for tv in Parties.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in PositionQty.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in PositionAmountData.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if PosReqID != None:
		msg.append_pair(710,PosReqID)
	if PosReqType != None:
		msg.append_pair(724,PosReqType)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if TotalNumPosReports != None:
		msg.append_pair(727,TotalNumPosReports)
	if UnsolicitedIndicator != None:
		msg.append_pair(325,UnsolicitedIndicator)
	if SettlSessID != None:
		msg.append_pair(716,SettlSessID)
	if SettlSessSubID != None:
		msg.append_pair(717,SettlSessSubID)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if Currency != None:
		msg.append_pair(15,Currency)
	if RegistStatus != None:
		msg.append_pair(506,RegistStatus)
	if DeliveryDate != None:
		msg.append_pair(743,DeliveryDate)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if PosUndInstrmtGrp != None:
		for tv in PosUndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def TradeCaptureReportRequestAck(MsgSeqNum,TargetCompID,TradeRequestID,TradeRequestType,TradeRequestResult,TradeRequestStatus,Instrument,SubscriptionRequestType=None,TotNumTradeReports=None,MultiLegReportingType=None,ResponseTransportType=None,ResponseDestination=None,Text=None,EncodedTextLen=None,EncodedText=None,UndInstrmtGrp=None,InstrmtLegGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AQ,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(568,TradeRequestID)
	msg.append_pair(569,TradeRequestType)
	msg.append_pair(749,TradeRequestResult)
	msg.append_pair(750,TradeRequestStatus)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if TotNumTradeReports != None:
		msg.append_pair(748,TotNumTradeReports)
	if MultiLegReportingType != None:
		msg.append_pair(442,MultiLegReportingType)
	if ResponseTransportType != None:
		msg.append_pair(725,ResponseTransportType)
	if ResponseDestination != None:
		msg.append_pair(726,ResponseDestination)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def TradeCaptureReportAck(MsgSeqNum,TargetCompID,TradeReportID,ExecType,Instrument,TradeReportTransType=None,TradeReportType=None,TrdType=None,TrdSubType=None,SecondaryTrdType=None,TransferReason=None,TradeReportRefID=None,SecondaryTradeReportRefID=None,TrdRptStatus=None,TradeReportRejectReason=None,SecondaryTradeReportID=None,SubscriptionRequestType=None,TradeLinkID=None,TrdMatchID=None,ExecID=None,SecondaryExecID=None,TransactTime=None,ResponseTransportType=None,ResponseDestination=None,Text=None,EncodedTextLen=None,EncodedText=None,ClearingFeeIndicator=None,OrderCapacity=None,OrderRestrictions=None,CustOrderCapacity=None,Account=None,AcctIDSource=None,AccountType=None,PositionEffect=None,PreallocMethod=None,TrdRegTimestamps=None,TrdInstrmtLegGrp=None,TrdAllocGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AR,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(571,TradeReportID)
	msg.append_pair(150,ExecType)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if TradeReportTransType != None:
		msg.append_pair(487,TradeReportTransType)
	if TradeReportType != None:
		msg.append_pair(856,TradeReportType)
	if TrdType != None:
		msg.append_pair(828,TrdType)
	if TrdSubType != None:
		msg.append_pair(829,TrdSubType)
	if SecondaryTrdType != None:
		msg.append_pair(855,SecondaryTrdType)
	if TransferReason != None:
		msg.append_pair(830,TransferReason)
	if TradeReportRefID != None:
		msg.append_pair(572,TradeReportRefID)
	if SecondaryTradeReportRefID != None:
		msg.append_pair(881,SecondaryTradeReportRefID)
	if TrdRptStatus != None:
		msg.append_pair(939,TrdRptStatus)
	if TradeReportRejectReason != None:
		msg.append_pair(751,TradeReportRejectReason)
	if SecondaryTradeReportID != None:
		msg.append_pair(818,SecondaryTradeReportID)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if TradeLinkID != None:
		msg.append_pair(820,TradeLinkID)
	if TrdMatchID != None:
		msg.append_pair(880,TrdMatchID)
	if ExecID != None:
		msg.append_pair(17,ExecID)
	if SecondaryExecID != None:
		msg.append_pair(527,SecondaryExecID)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if ResponseTransportType != None:
		msg.append_pair(725,ResponseTransportType)
	if ResponseDestination != None:
		msg.append_pair(726,ResponseDestination)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if ClearingFeeIndicator != None:
		msg.append_pair(635,ClearingFeeIndicator)
	if OrderCapacity != None:
		msg.append_pair(528,OrderCapacity)
	if OrderRestrictions != None:
		msg.append_pair(529,OrderRestrictions)
	if CustOrderCapacity != None:
		msg.append_pair(582,CustOrderCapacity)
	if Account != None:
		msg.append_pair(1,Account)
	if AcctIDSource != None:
		msg.append_pair(660,AcctIDSource)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if PositionEffect != None:
		msg.append_pair(77,PositionEffect)
	if PreallocMethod != None:
		msg.append_pair(591,PreallocMethod)
	if TrdRegTimestamps != None:
		for tv in TrdRegTimestamps.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdInstrmtLegGrp != None:
		for tv in TrdInstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdAllocGrp != None:
		for tv in TrdAllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def AllocationReport(MsgSeqNum,TargetCompID,AllocReportID,AllocTransType,AllocReportType,AllocStatus,AllocNoOrdersType,Side,Quantity,AvgPx,TradeDate,Instrument,AllocID=None,AllocReportRefID=None,AllocCancReplaceReason=None,SecondaryAllocID=None,AllocRejCode=None,RefAllocID=None,AllocIntermedReqType=None,AllocLinkID=None,AllocLinkType=None,BookingRefID=None,PreviouslyReported=None,ReversalIndicator=None,MatchType=None,QtyType=None,LastMkt=None,TradeOriginationDate=None,TradingSessionID=None,TradingSessionSubID=None,PriceType=None,AvgParPx=None,Currency=None,AvgPxPrecision=None,TransactTime=None,SettlType=None,SettlDate=None,BookingType=None,GrossTradeAmt=None,Concession=None,TotalTakedown=None,NetMoney=None,PositionEffect=None,AutoAcceptIndicator=None,Text=None,EncodedTextLen=None,EncodedText=None,NumDaysInterest=None,AccruedInterestRate=None,AccruedInterestAmt=None,TotalAccruedInterestAmt=None,InterestAtMaturity=None,EndAccruedInterestAmt=None,StartCash=None,EndCash=None,LegalConfirm=None,TotNoAllocs=None,LastFragment=None,OrdAllocGrp=None,ExecAllocGrp=None,InstrumentExtension=None,FinancingDetails=None,UndInstrmtGrp=None,InstrmtLegGrp=None,SpreadOrBenchmarkCurveData=None,Parties=None,Stipulations=None,YieldData=None,AllocGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AS,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(755,AllocReportID)
	msg.append_pair(71,AllocTransType)
	msg.append_pair(794,AllocReportType)
	msg.append_pair(87,AllocStatus)
	msg.append_pair(857,AllocNoOrdersType)
	msg.append_pair(54,Side)
	msg.append_pair(53,Quantity)
	msg.append_pair(6,AvgPx)
	msg.append_pair(75,TradeDate)
	for tv in Instrument.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if AllocID != None:
		msg.append_pair(70,AllocID)
	if AllocReportRefID != None:
		msg.append_pair(795,AllocReportRefID)
	if AllocCancReplaceReason != None:
		msg.append_pair(796,AllocCancReplaceReason)
	if SecondaryAllocID != None:
		msg.append_pair(793,SecondaryAllocID)
	if AllocRejCode != None:
		msg.append_pair(88,AllocRejCode)
	if RefAllocID != None:
		msg.append_pair(72,RefAllocID)
	if AllocIntermedReqType != None:
		msg.append_pair(808,AllocIntermedReqType)
	if AllocLinkID != None:
		msg.append_pair(196,AllocLinkID)
	if AllocLinkType != None:
		msg.append_pair(197,AllocLinkType)
	if BookingRefID != None:
		msg.append_pair(466,BookingRefID)
	if PreviouslyReported != None:
		msg.append_pair(570,PreviouslyReported)
	if ReversalIndicator != None:
		msg.append_pair(700,ReversalIndicator)
	if MatchType != None:
		msg.append_pair(574,MatchType)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if LastMkt != None:
		msg.append_pair(30,LastMkt)
	if TradeOriginationDate != None:
		msg.append_pair(229,TradeOriginationDate)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if AvgParPx != None:
		msg.append_pair(860,AvgParPx)
	if Currency != None:
		msg.append_pair(15,Currency)
	if AvgPxPrecision != None:
		msg.append_pair(74,AvgPxPrecision)
	if TransactTime != None:
		msg.append_pair(60,TransactTime)
	if SettlType != None:
		msg.append_pair(63,SettlType)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if BookingType != None:
		msg.append_pair(775,BookingType)
	if GrossTradeAmt != None:
		msg.append_pair(381,GrossTradeAmt)
	if Concession != None:
		msg.append_pair(238,Concession)
	if TotalTakedown != None:
		msg.append_pair(237,TotalTakedown)
	if NetMoney != None:
		msg.append_pair(118,NetMoney)
	if PositionEffect != None:
		msg.append_pair(77,PositionEffect)
	if AutoAcceptIndicator != None:
		msg.append_pair(754,AutoAcceptIndicator)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if NumDaysInterest != None:
		msg.append_pair(157,NumDaysInterest)
	if AccruedInterestRate != None:
		msg.append_pair(158,AccruedInterestRate)
	if AccruedInterestAmt != None:
		msg.append_pair(159,AccruedInterestAmt)
	if TotalAccruedInterestAmt != None:
		msg.append_pair(540,TotalAccruedInterestAmt)
	if InterestAtMaturity != None:
		msg.append_pair(738,InterestAtMaturity)
	if EndAccruedInterestAmt != None:
		msg.append_pair(920,EndAccruedInterestAmt)
	if StartCash != None:
		msg.append_pair(921,StartCash)
	if EndCash != None:
		msg.append_pair(922,EndCash)
	if LegalConfirm != None:
		msg.append_pair(650,LegalConfirm)
	if TotNoAllocs != None:
		msg.append_pair(892,TotNoAllocs)
	if LastFragment != None:
		msg.append_pair(893,LastFragment)
	if OrdAllocGrp != None:
		for tv in OrdAllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ExecAllocGrp != None:
		for tv in ExecAllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrumentExtension != None:
		for tv in InstrumentExtension.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if YieldData != None:
		for tv in YieldData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if AllocGrp != None:
		for tv in AllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def AllocationReportAck(MsgSeqNum,TargetCompID,AllocReportID,AllocID,TransactTime,AllocStatus,SecondaryAllocID=None,TradeDate=None,AllocRejCode=None,AllocReportType=None,AllocIntermedReqType=None,MatchStatus=None,Product=None,SecurityType=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,AllocAckGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AT,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(755,AllocReportID)
	msg.append_pair(70,AllocID)
	msg.append_pair(60,TransactTime)
	msg.append_pair(87,AllocStatus)
	if SecondaryAllocID != None:
		msg.append_pair(793,SecondaryAllocID)
	if TradeDate != None:
		msg.append_pair(75,TradeDate)
	if AllocRejCode != None:
		msg.append_pair(88,AllocRejCode)
	if AllocReportType != None:
		msg.append_pair(794,AllocReportType)
	if AllocIntermedReqType != None:
		msg.append_pair(808,AllocIntermedReqType)
	if MatchStatus != None:
		msg.append_pair(573,MatchStatus)
	if Product != None:
		msg.append_pair(460,Product)
	if SecurityType != None:
		msg.append_pair(167,SecurityType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if AllocAckGrp != None:
		for tv in AllocAckGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def ConfirmationAck(MsgSeqNum,TargetCompID,ConfirmID,TradeDate,TransactTime,AffirmStatus,ConfirmRejReason=None,MatchStatus=None,Text=None,EncodedTextLen=None,EncodedText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AU,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(664,ConfirmID)
	msg.append_pair(75,TradeDate)
	msg.append_pair(60,TransactTime)
	msg.append_pair(940,AffirmStatus)
	if ConfirmRejReason != None:
		msg.append_pair(774,ConfirmRejReason)
	if MatchStatus != None:
		msg.append_pair(573,MatchStatus)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	return msg.encode()

def SettlementInstructionRequest(MsgSeqNum,TargetCompID,SettlInstReqID,TransactTime,AllocAccount=None,AllocAcctIDSource=None,Side=None,Product=None,SecurityType=None,CFICode=None,EffectiveTime=None,ExpireTime=None,LastUpdateTime=None,StandInstDbType=None,StandInstDbName=None,StandInstDbID=None,Parties=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AV,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(791,SettlInstReqID)
	msg.append_pair(60,TransactTime)
	if AllocAccount != None:
		msg.append_pair(79,AllocAccount)
	if AllocAcctIDSource != None:
		msg.append_pair(661,AllocAcctIDSource)
	if Side != None:
		msg.append_pair(54,Side)
	if Product != None:
		msg.append_pair(460,Product)
	if SecurityType != None:
		msg.append_pair(167,SecurityType)
	if CFICode != None:
		msg.append_pair(461,CFICode)
	if EffectiveTime != None:
		msg.append_pair(168,EffectiveTime)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if LastUpdateTime != None:
		msg.append_pair(779,LastUpdateTime)
	if StandInstDbType != None:
		msg.append_pair(169,StandInstDbType)
	if StandInstDbName != None:
		msg.append_pair(170,StandInstDbName)
	if StandInstDbID != None:
		msg.append_pair(171,StandInstDbID)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def AssignmentReport(MsgSeqNum,TargetCompID,AsgnRptID,AccountType,SettlPrice,SettlPriceType,UnderlyingSettlPrice,AssignmentMethod,OpenInterest,ExerciseMethod,SettlSessID,SettlSessSubID,ClearingBusinessDate,Parties,PositionQty,PositionAmountData,TotNumAssignmentReports=None,LastRptRequested=None,Account=None,Currency=None,ThresholdAmount=None,ExpireDate=None,AssignmentUnit=None,Text=None,EncodedTextLen=None,EncodedText=None,Instrument=None,InstrmtLegGrp=None,UndInstrmtGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AW,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(833,AsgnRptID)
	msg.append_pair(581,AccountType)
	msg.append_pair(730,SettlPrice)
	msg.append_pair(731,SettlPriceType)
	msg.append_pair(732,UnderlyingSettlPrice)
	msg.append_pair(744,AssignmentMethod)
	msg.append_pair(746,OpenInterest)
	msg.append_pair(747,ExerciseMethod)
	msg.append_pair(716,SettlSessID)
	msg.append_pair(717,SettlSessSubID)
	msg.append_pair(715,ClearingBusinessDate)
	for tv in Parties.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in PositionQty.tag_vals:
		msg.append_pair(tv[0],tv[1])
	for tv in PositionAmountData.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if TotNumAssignmentReports != None:
		msg.append_pair(832,TotNumAssignmentReports)
	if LastRptRequested != None:
		msg.append_pair(912,LastRptRequested)
	if Account != None:
		msg.append_pair(1,Account)
	if Currency != None:
		msg.append_pair(15,Currency)
	if ThresholdAmount != None:
		msg.append_pair(834,ThresholdAmount)
	if ExpireDate != None:
		msg.append_pair(432,ExpireDate)
	if AssignmentUnit != None:
		msg.append_pair(745,AssignmentUnit)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def CollateralRequest(MsgSeqNum,TargetCompID,CollReqID,CollAsgnReason,TransactTime,ExpireTime=None,Account=None,AccountType=None,ClOrdID=None,OrderID=None,SecondaryOrderID=None,SecondaryClOrdID=None,SettlDate=None,Quantity=None,QtyType=None,Currency=None,MarginExcess=None,TotalNetValue=None,CashOutstanding=None,Side=None,Price=None,PriceType=None,AccruedInterestAmt=None,EndAccruedInterestAmt=None,StartCash=None,EndCash=None,TradingSessionID=None,TradingSessionSubID=None,SettlSessID=None,SettlSessSubID=None,ClearingBusinessDate=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,ExecCollGrp=None,TrdCollGrp=None,Instrument=None,FinancingDetails=None,InstrmtLegGrp=None,UndInstrmtCollGrp=None,TrdRegTimestamps=None,MiscFeesGrp=None,SpreadOrBenchmarkCurveData=None,Stipulations=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AX,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(894,CollReqID)
	msg.append_pair(895,CollAsgnReason)
	msg.append_pair(60,TransactTime)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if Account != None:
		msg.append_pair(1,Account)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if Quantity != None:
		msg.append_pair(53,Quantity)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if MarginExcess != None:
		msg.append_pair(899,MarginExcess)
	if TotalNetValue != None:
		msg.append_pair(900,TotalNetValue)
	if CashOutstanding != None:
		msg.append_pair(901,CashOutstanding)
	if Side != None:
		msg.append_pair(54,Side)
	if Price != None:
		msg.append_pair(44,Price)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if AccruedInterestAmt != None:
		msg.append_pair(159,AccruedInterestAmt)
	if EndAccruedInterestAmt != None:
		msg.append_pair(920,EndAccruedInterestAmt)
	if StartCash != None:
		msg.append_pair(921,StartCash)
	if EndCash != None:
		msg.append_pair(922,EndCash)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if SettlSessID != None:
		msg.append_pair(716,SettlSessID)
	if SettlSessSubID != None:
		msg.append_pair(717,SettlSessSubID)
	if ClearingBusinessDate != None:
		msg.append_pair(715,ClearingBusinessDate)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ExecCollGrp != None:
		for tv in ExecCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdCollGrp != None:
		for tv in TrdCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtCollGrp != None:
		for tv in UndInstrmtCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdRegTimestamps != None:
		for tv in TrdRegTimestamps.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if MiscFeesGrp != None:
		for tv in MiscFeesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def CollateralAssignment(MsgSeqNum,TargetCompID,CollAsgnID,CollAsgnReason,CollAsgnTransType,TransactTime,CollReqID=None,CollAsgnRefID=None,ExpireTime=None,Account=None,AccountType=None,ClOrdID=None,OrderID=None,SecondaryOrderID=None,SecondaryClOrdID=None,SettlDate=None,Quantity=None,QtyType=None,Currency=None,MarginExcess=None,TotalNetValue=None,CashOutstanding=None,Side=None,Price=None,PriceType=None,AccruedInterestAmt=None,EndAccruedInterestAmt=None,StartCash=None,EndCash=None,TradingSessionID=None,TradingSessionSubID=None,SettlSessID=None,SettlSessSubID=None,ClearingBusinessDate=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,ExecCollGrp=None,TrdCollGrp=None,Instrument=None,FinancingDetails=None,InstrmtLegGrp=None,UndInstrmtCollGrp=None,TrdRegTimestamps=None,MiscFeesGrp=None,SpreadOrBenchmarkCurveData=None,Stipulations=None,SettlInstructionsData=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AY,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(902,CollAsgnID)
	msg.append_pair(895,CollAsgnReason)
	msg.append_pair(903,CollAsgnTransType)
	msg.append_pair(60,TransactTime)
	if CollReqID != None:
		msg.append_pair(894,CollReqID)
	if CollAsgnRefID != None:
		msg.append_pair(907,CollAsgnRefID)
	if ExpireTime != None:
		msg.append_pair(126,ExpireTime)
	if Account != None:
		msg.append_pair(1,Account)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if Quantity != None:
		msg.append_pair(53,Quantity)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if MarginExcess != None:
		msg.append_pair(899,MarginExcess)
	if TotalNetValue != None:
		msg.append_pair(900,TotalNetValue)
	if CashOutstanding != None:
		msg.append_pair(901,CashOutstanding)
	if Side != None:
		msg.append_pair(54,Side)
	if Price != None:
		msg.append_pair(44,Price)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if AccruedInterestAmt != None:
		msg.append_pair(159,AccruedInterestAmt)
	if EndAccruedInterestAmt != None:
		msg.append_pair(920,EndAccruedInterestAmt)
	if StartCash != None:
		msg.append_pair(921,StartCash)
	if EndCash != None:
		msg.append_pair(922,EndCash)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if SettlSessID != None:
		msg.append_pair(716,SettlSessID)
	if SettlSessSubID != None:
		msg.append_pair(717,SettlSessSubID)
	if ClearingBusinessDate != None:
		msg.append_pair(715,ClearingBusinessDate)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ExecCollGrp != None:
		for tv in ExecCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdCollGrp != None:
		for tv in TrdCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtCollGrp != None:
		for tv in UndInstrmtCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdRegTimestamps != None:
		for tv in TrdRegTimestamps.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if MiscFeesGrp != None:
		for tv in MiscFeesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SettlInstructionsData != None:
		for tv in SettlInstructionsData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def CollateralResponse(MsgSeqNum,TargetCompID,CollRespID,CollAsgnID,CollAsgnReason,CollAsgnRespType,TransactTime,CollReqID=None,CollAsgnTransType=None,CollAsgnRejectReason=None,Account=None,AccountType=None,ClOrdID=None,OrderID=None,SecondaryOrderID=None,SecondaryClOrdID=None,SettlDate=None,Quantity=None,QtyType=None,Currency=None,MarginExcess=None,TotalNetValue=None,CashOutstanding=None,Side=None,Price=None,PriceType=None,AccruedInterestAmt=None,EndAccruedInterestAmt=None,StartCash=None,EndCash=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,ExecCollGrp=None,TrdCollGrp=None,Instrument=None,FinancingDetails=None,InstrmtLegGrp=None,UndInstrmtCollGrp=None,TrdRegTimestamps=None,MiscFeesGrp=None,SpreadOrBenchmarkCurveData=None,Stipulations=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,AZ,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(904,CollRespID)
	msg.append_pair(902,CollAsgnID)
	msg.append_pair(895,CollAsgnReason)
	msg.append_pair(905,CollAsgnRespType)
	msg.append_pair(60,TransactTime)
	if CollReqID != None:
		msg.append_pair(894,CollReqID)
	if CollAsgnTransType != None:
		msg.append_pair(903,CollAsgnTransType)
	if CollAsgnRejectReason != None:
		msg.append_pair(906,CollAsgnRejectReason)
	if Account != None:
		msg.append_pair(1,Account)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if Quantity != None:
		msg.append_pair(53,Quantity)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if MarginExcess != None:
		msg.append_pair(899,MarginExcess)
	if TotalNetValue != None:
		msg.append_pair(900,TotalNetValue)
	if CashOutstanding != None:
		msg.append_pair(901,CashOutstanding)
	if Side != None:
		msg.append_pair(54,Side)
	if Price != None:
		msg.append_pair(44,Price)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if AccruedInterestAmt != None:
		msg.append_pair(159,AccruedInterestAmt)
	if EndAccruedInterestAmt != None:
		msg.append_pair(920,EndAccruedInterestAmt)
	if StartCash != None:
		msg.append_pair(921,StartCash)
	if EndCash != None:
		msg.append_pair(922,EndCash)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ExecCollGrp != None:
		for tv in ExecCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdCollGrp != None:
		for tv in TrdCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtCollGrp != None:
		for tv in UndInstrmtCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdRegTimestamps != None:
		for tv in TrdRegTimestamps.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if MiscFeesGrp != None:
		for tv in MiscFeesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def CollateralReport(MsgSeqNum,TargetCompID,CollRptID,CollStatus,CollInquiryID=None,TotNumReports=None,LastRptRequested=None,Account=None,AccountType=None,ClOrdID=None,OrderID=None,SecondaryOrderID=None,SecondaryClOrdID=None,SettlDate=None,Quantity=None,QtyType=None,Currency=None,MarginExcess=None,TotalNetValue=None,CashOutstanding=None,Side=None,Price=None,PriceType=None,AccruedInterestAmt=None,EndAccruedInterestAmt=None,StartCash=None,EndCash=None,TradingSessionID=None,TradingSessionSubID=None,SettlSessID=None,SettlSessSubID=None,ClearingBusinessDate=None,Text=None,EncodedTextLen=None,EncodedText=None,Parties=None,ExecCollGrp=None,TrdCollGrp=None,Instrument=None,FinancingDetails=None,InstrmtLegGrp=None,UndInstrmtGrp=None,TrdRegTimestamps=None,MiscFeesGrp=None,SpreadOrBenchmarkCurveData=None,Stipulations=None,SettlInstructionsData=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,BA,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(908,CollRptID)
	msg.append_pair(910,CollStatus)
	if CollInquiryID != None:
		msg.append_pair(909,CollInquiryID)
	if TotNumReports != None:
		msg.append_pair(911,TotNumReports)
	if LastRptRequested != None:
		msg.append_pair(912,LastRptRequested)
	if Account != None:
		msg.append_pair(1,Account)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if Quantity != None:
		msg.append_pair(53,Quantity)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if MarginExcess != None:
		msg.append_pair(899,MarginExcess)
	if TotalNetValue != None:
		msg.append_pair(900,TotalNetValue)
	if CashOutstanding != None:
		msg.append_pair(901,CashOutstanding)
	if Side != None:
		msg.append_pair(54,Side)
	if Price != None:
		msg.append_pair(44,Price)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if AccruedInterestAmt != None:
		msg.append_pair(159,AccruedInterestAmt)
	if EndAccruedInterestAmt != None:
		msg.append_pair(920,EndAccruedInterestAmt)
	if StartCash != None:
		msg.append_pair(921,StartCash)
	if EndCash != None:
		msg.append_pair(922,EndCash)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if SettlSessID != None:
		msg.append_pair(716,SettlSessID)
	if SettlSessSubID != None:
		msg.append_pair(717,SettlSessSubID)
	if ClearingBusinessDate != None:
		msg.append_pair(715,ClearingBusinessDate)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ExecCollGrp != None:
		for tv in ExecCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdCollGrp != None:
		for tv in TrdCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdRegTimestamps != None:
		for tv in TrdRegTimestamps.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if MiscFeesGrp != None:
		for tv in MiscFeesGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SettlInstructionsData != None:
		for tv in SettlInstructionsData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def CollateralInquiry(MsgSeqNum,TargetCompID,CollInquiryID=None,SubscriptionRequestType=None,ResponseTransportType=None,ResponseDestination=None,Account=None,AccountType=None,ClOrdID=None,OrderID=None,SecondaryOrderID=None,SecondaryClOrdID=None,SettlDate=None,Quantity=None,QtyType=None,Currency=None,MarginExcess=None,TotalNetValue=None,CashOutstanding=None,Side=None,Price=None,PriceType=None,AccruedInterestAmt=None,EndAccruedInterestAmt=None,StartCash=None,EndCash=None,TradingSessionID=None,TradingSessionSubID=None,SettlSessID=None,SettlSessSubID=None,ClearingBusinessDate=None,Text=None,EncodedTextLen=None,EncodedText=None,CollInqQualGrp=None,Parties=None,ExecCollGrp=None,TrdCollGrp=None,Instrument=None,FinancingDetails=None,InstrmtLegGrp=None,UndInstrmtGrp=None,TrdRegTimestamps=None,SpreadOrBenchmarkCurveData=None,Stipulations=None,SettlInstructionsData=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,BB,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	if CollInquiryID != None:
		msg.append_pair(909,CollInquiryID)
	if SubscriptionRequestType != None:
		msg.append_pair(263,SubscriptionRequestType)
	if ResponseTransportType != None:
		msg.append_pair(725,ResponseTransportType)
	if ResponseDestination != None:
		msg.append_pair(726,ResponseDestination)
	if Account != None:
		msg.append_pair(1,Account)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if Quantity != None:
		msg.append_pair(53,Quantity)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if MarginExcess != None:
		msg.append_pair(899,MarginExcess)
	if TotalNetValue != None:
		msg.append_pair(900,TotalNetValue)
	if CashOutstanding != None:
		msg.append_pair(901,CashOutstanding)
	if Side != None:
		msg.append_pair(54,Side)
	if Price != None:
		msg.append_pair(44,Price)
	if PriceType != None:
		msg.append_pair(423,PriceType)
	if AccruedInterestAmt != None:
		msg.append_pair(159,AccruedInterestAmt)
	if EndAccruedInterestAmt != None:
		msg.append_pair(920,EndAccruedInterestAmt)
	if StartCash != None:
		msg.append_pair(921,StartCash)
	if EndCash != None:
		msg.append_pair(922,EndCash)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if SettlSessID != None:
		msg.append_pair(716,SettlSessID)
	if SettlSessSubID != None:
		msg.append_pair(717,SettlSessSubID)
	if ClearingBusinessDate != None:
		msg.append_pair(715,ClearingBusinessDate)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if CollInqQualGrp != None:
		for tv in CollInqQualGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ExecCollGrp != None:
		for tv in ExecCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdCollGrp != None:
		for tv in TrdCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdRegTimestamps != None:
		for tv in TrdRegTimestamps.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SpreadOrBenchmarkCurveData != None:
		for tv in SpreadOrBenchmarkCurveData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Stipulations != None:
		for tv in Stipulations.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if SettlInstructionsData != None:
		for tv in SettlInstructionsData.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def NetworkCounterpartySystemStatusRequest(MsgSeqNum,TargetCompID,NetworkRequestType,NetworkRequestID,CompIDReqGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,BC,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(935,NetworkRequestType)
	msg.append_pair(933,NetworkRequestID)
	if CompIDReqGrp != None:
		for tv in CompIDReqGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def NetworkCounterpartySystemStatusResponse(MsgSeqNum,TargetCompID,NetworkStatusResponseType,NetworkResponseID,CompIDStatGrp,NetworkRequestID=None,LastNetworkResponseID=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,BD,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(937,NetworkStatusResponseType)
	msg.append_pair(932,NetworkResponseID)
	for tv in CompIDStatGrp.tag_vals:
		msg.append_pair(tv[0],tv[1])
	if NetworkRequestID != None:
		msg.append_pair(933,NetworkRequestID)
	if LastNetworkResponseID != None:
		msg.append_pair(934,LastNetworkResponseID)
	return msg.encode()

def UserRequest(MsgSeqNum,TargetCompID,UserRequestID,UserRequestType,Username,Password=None,NewPassword=None,RawDataLength=None,RawData=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,BE,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(923,UserRequestID)
	msg.append_pair(924,UserRequestType)
	msg.append_pair(553,Username)
	if Password != None:
		msg.append_pair(554,Password)
	if NewPassword != None:
		msg.append_pair(925,NewPassword)
	if RawDataLength != None:
		msg.append_pair(95,RawDataLength)
	if RawData != None:
		msg.append_pair(96,RawData)
	return msg.encode()

def UserResponse(MsgSeqNum,TargetCompID,UserRequestID,Username,UserStatus=None,UserStatusText=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,BF,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(923,UserRequestID)
	msg.append_pair(553,Username)
	if UserStatus != None:
		msg.append_pair(926,UserStatus)
	if UserStatusText != None:
		msg.append_pair(927,UserStatusText)
	return msg.encode()

def CollateralInquiryAck(MsgSeqNum,TargetCompID,CollInquiryID,CollInquiryStatus,CollInquiryResult=None,TotNumReports=None,Account=None,AccountType=None,ClOrdID=None,OrderID=None,SecondaryOrderID=None,SecondaryClOrdID=None,SettlDate=None,Quantity=None,QtyType=None,Currency=None,TradingSessionID=None,TradingSessionSubID=None,SettlSessID=None,SettlSessSubID=None,ClearingBusinessDate=None,ResponseTransportType=None,ResponseDestination=None,Text=None,EncodedTextLen=None,EncodedText=None,CollInqQualGrp=None,Parties=None,ExecCollGrp=None,TrdCollGrp=None,Instrument=None,FinancingDetails=None,InstrmtLegGrp=None,UndInstrmtGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,BG,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(909,CollInquiryID)
	msg.append_pair(945,CollInquiryStatus)
	if CollInquiryResult != None:
		msg.append_pair(946,CollInquiryResult)
	if TotNumReports != None:
		msg.append_pair(911,TotNumReports)
	if Account != None:
		msg.append_pair(1,Account)
	if AccountType != None:
		msg.append_pair(581,AccountType)
	if ClOrdID != None:
		msg.append_pair(11,ClOrdID)
	if OrderID != None:
		msg.append_pair(37,OrderID)
	if SecondaryOrderID != None:
		msg.append_pair(198,SecondaryOrderID)
	if SecondaryClOrdID != None:
		msg.append_pair(526,SecondaryClOrdID)
	if SettlDate != None:
		msg.append_pair(64,SettlDate)
	if Quantity != None:
		msg.append_pair(53,Quantity)
	if QtyType != None:
		msg.append_pair(854,QtyType)
	if Currency != None:
		msg.append_pair(15,Currency)
	if TradingSessionID != None:
		msg.append_pair(336,TradingSessionID)
	if TradingSessionSubID != None:
		msg.append_pair(625,TradingSessionSubID)
	if SettlSessID != None:
		msg.append_pair(716,SettlSessID)
	if SettlSessSubID != None:
		msg.append_pair(717,SettlSessSubID)
	if ClearingBusinessDate != None:
		msg.append_pair(715,ClearingBusinessDate)
	if ResponseTransportType != None:
		msg.append_pair(725,ResponseTransportType)
	if ResponseDestination != None:
		msg.append_pair(726,ResponseDestination)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if CollInqQualGrp != None:
		for tv in CollInqQualGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Parties != None:
		for tv in Parties.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if ExecCollGrp != None:
		for tv in ExecCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if TrdCollGrp != None:
		for tv in TrdCollGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if Instrument != None:
		for tv in Instrument.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if FinancingDetails != None:
		for tv in FinancingDetails.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if InstrmtLegGrp != None:
		for tv in InstrmtLegGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	if UndInstrmtGrp != None:
		for tv in UndInstrmtGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

def ConfirmationRequest(MsgSeqNum,TargetCompID,ConfirmReqID,ConfirmType,TransactTime,AllocID=None,SecondaryAllocID=None,IndividualAllocID=None,AllocAccount=None,AllocAcctIDSource=None,AllocAccountType=None,Text=None,EncodedTextLen=None,EncodedText=None,OrdAllocGrp=None):
	msg=simplefix.FixMessage()
	msg.append_pair(8,"FIX.4.4",header=True)
	msg.append_pair(35,BH,header=True)
	msg.append_pair(49,SENDER_COMP_ID,header=True)
	msg.append_pair(34,MsgSeqNum,header=True)
	msg.append_pair(56,TargetCompID,header=True)
	msg.append_pair(859,ConfirmReqID)
	msg.append_pair(773,ConfirmType)
	msg.append_pair(60,TransactTime)
	if AllocID != None:
		msg.append_pair(70,AllocID)
	if SecondaryAllocID != None:
		msg.append_pair(793,SecondaryAllocID)
	if IndividualAllocID != None:
		msg.append_pair(467,IndividualAllocID)
	if AllocAccount != None:
		msg.append_pair(79,AllocAccount)
	if AllocAcctIDSource != None:
		msg.append_pair(661,AllocAcctIDSource)
	if AllocAccountType != None:
		msg.append_pair(798,AllocAccountType)
	if Text != None:
		msg.append_pair(58,Text)
	if EncodedTextLen != None:
		msg.append_pair(354,EncodedTextLen)
	if EncodedText != None:
		msg.append_pair(355,EncodedText)
	if OrdAllocGrp != None:
		for tv in OrdAllocGrp.tag_vals:
			msg.append_pair(tv[0],tv[1])
	return msg.encode()

