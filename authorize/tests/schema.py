SCHEMA = """\
<?xml version="1.0" encoding="utf-8"?>
<xs:schema targetNamespace="AnetApi/xml/v1/schema/AnetApiSchema.xsd" elementFormDefault="qualified" xmlns:anet="AnetApi/xml/v1/schema/AnetApiSchema.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<!-- 
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	 Request type definitions begin here
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	-->
	<xs:simpleType name="numericString">
		<xs:restriction base="xs:string">
			<xs:pattern value="[0-9]+" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="bankAccountTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="checking" />
			<xs:enumeration value="savings" />
			<xs:enumeration value="businessChecking" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="echeckTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="PPD" />
			<xs:enumeration value="WEB" />
			<xs:enumeration value="CCD" />
			<xs:enumeration value="TEL" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="customerTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="individual" />
			<xs:enumeration value="business" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="ARBSubscriptionUnitEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="days" />
			<xs:enumeration value="months" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<xs:simpleType name="validationModeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="none" />
			<xs:enumeration value="testMode" />
			<xs:enumeration value="liveMode" />
		</xs:restriction>
	</xs:simpleType>
	<!-- ===================================================== -->
	<!--xs:complexType name="driversLicenseBaseType">
		<xs:sequence>
			<xs:element name="state">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="2" />
						<xs:maxLength value="2" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType-->
	<!-- ===================================================== -->
	<xs:complexType name="driversLicenseType">
		<xs:sequence>
			<xs:element name="number">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="5" />
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="state">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="2" />
						<xs:maxLength value="2" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="dateOfBirth">
				<xs:simpleType>
					<xs:restriction base="xs:date">
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="driversLicenseMaskedType">
		<xs:sequence>
			<xs:element name="number">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:length value="8" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="state">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="2" />
						<xs:maxLength value="2" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="dateOfBirth">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="8" />
						<xs:maxLength value="10" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="nameAndAddressType">
		<xs:sequence>
			<xs:element name="firstName" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="lastName" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="company" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="address" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="60" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="city" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="40" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="state" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="40" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="zip" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="country" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="60" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="creditCardSimpleType">
		<xs:sequence>
			<!-- Format of cardNumber should be numeric or four X's followed by the last four digits. -->
			<xs:element name="cardNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="8" />
						<xs:maxLength value="16" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- Format of expirationDate should be gYearMonth (such as 2001-10) or X's. -->
			<xs:element name="expirationDate">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="4" />
						<xs:maxLength value="7" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="creditCardType">
		<xs:complexContent>
			<xs:extension base="anet:creditCardSimpleType">
				<xs:sequence>
					<xs:element name="cardCode" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="anet:numericString">
								<xs:minLength value="3" />
								<xs:maxLength value="4" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="creditCardMaskedType">
		<xs:sequence>
			<xs:element name="cardNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:length value="8" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="expirationDate">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="4" />
						<xs:maxLength value="7" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<!--xs:complexType name="bankAccountBaseType">
		<xs:sequence>
			<xs:element name="accountType" type="anet:bankAccountTypeEnum" minOccurs="0" />
			<xs:element name="nameOnAccount">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="22" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="echeckType" type="anet:echeckTypeEnum" minOccurs="0" />
			<xs:element name="bankName" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType-->
	<!-- ===================================================== -->
	<xs:complexType name="bankAccountType">
		<xs:sequence>
			<xs:element name="accountType" type="anet:bankAccountTypeEnum" minOccurs="0" />
			<!-- Format of routingNumber should be nine digits or four X's followed by the last four digits. -->
			<xs:element name="routingNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="8" />
						<xs:maxLength value="9" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- Format of accountNumber should be numeric or four X's followed by the last four digits. -->
			<xs:element name="accountNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="5" />
						<xs:maxLength value="17" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="nameOnAccount">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="22" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="echeckType" type="anet:echeckTypeEnum" minOccurs="0" />
			<xs:element name="bankName" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="bankAccountMaskedType">
		<xs:sequence>
			<xs:element name="accountType" type="anet:bankAccountTypeEnum" minOccurs="0" />
			<xs:element name="routingNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:length value="8" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="accountNumber">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:length value="8" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="nameOnAccount">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="22" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="echeckType" type="anet:echeckTypeEnum" minOccurs="0" />
			<xs:element name="bankName" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="paymentSimpleType">
		<xs:sequence>
			<xs:choice>
				<xs:element name="creditCard" type="anet:creditCardSimpleType" />
				<xs:element name="bankAccount" type="anet:bankAccountType" />
			</xs:choice>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="paymentType">
		<xs:sequence>
			<xs:choice>
				<xs:element name="creditCard" type="anet:creditCardType" />
				<xs:element name="bankAccount" type="anet:bankAccountType" />
			</xs:choice>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="paymentMaskedType">
		<xs:sequence>
			<xs:choice>
				<xs:element name="creditCard" type="anet:creditCardMaskedType" />
				<xs:element name="bankAccount" type="anet:bankAccountMaskedType" />
			</xs:choice>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="orderType">
		<xs:sequence>
			<xs:element name="invoiceNumber" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="description" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="orderExType">
		<xs:complexContent>
			<xs:extension base="anet:orderType">
				<xs:sequence>
					<xs:element name="purchaseOrderNumber" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:maxLength value="25" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerType">
		<xs:sequence>
			<xs:element name="type" type="anet:customerTypeEnum" minOccurs="0" />
			<xs:element name="id" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="email" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="phoneNumber" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="25" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="faxNumber" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="25" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="driversLicense" type="anet:driversLicenseType" minOccurs="0" />
			<xs:element name="taxId" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="anet:numericString">
						<xs:minLength value="9" />
						<xs:maxLength value="9" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="merchantAuthenticationType">
		<xs:sequence>
			<xs:element name="name">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="25" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="transactionKey">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="16" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="paymentScheduleType">
		<xs:sequence>
			<!-- required for a new schedule, optional when updating -->
			<xs:element name="interval" minOccurs="0">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="length">
							<xs:simpleType>
								<xs:restriction base="xs:short">
									<xs:minInclusive value="1" />
									<xs:maxInclusive value="32000" />
								</xs:restriction>
							</xs:simpleType>
						</xs:element>
						<xs:element name="unit" type="anet:ARBSubscriptionUnitEnum" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<!-- required for a new schedule, not allowed when editting existing subscription -->
			<xs:element name="startDate" type="xs:date" minOccurs="0" />
			<!-- required for a new schedule, optional when updating -->
			<xs:element name="totalOccurrences" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:short">
						<xs:minInclusive value="1" />
						<xs:maxInclusive value="32000" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- trialOccurrences is always optional -->
			<xs:element name="trialOccurrences" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:short">
						<xs:minInclusive value="0" />
						<xs:maxInclusive value="32000" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="ARBSubscriptionType">
		<xs:sequence>
			<xs:element name="name" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="50" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- paymentSchedule is required for a new subscription, optional if updating existing subscription -->
			<xs:element name="paymentSchedule" type="anet:paymentScheduleType" minOccurs="0" />
			<xs:element name="amount" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.01" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="trialAmount" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:fractionDigits value="4" />
						<xs:minInclusive value="0.00" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<!-- required for Create, optional on Update -->
			<xs:element name="payment" type="anet:paymentType" minOccurs="0" />
			<xs:element name="order" type="anet:orderType" minOccurs="0" />
			<xs:element name="customer" type="anet:customerType" minOccurs="0" />
			<xs:element name="billTo" type="anet:nameAndAddressType" minOccurs="0" />
			<xs:element name="shipTo" type="anet:nameAndAddressType" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerPaymentProfileBaseType">
		<xs:sequence>
			<xs:element name="customerType" type="anet:customerTypeEnum" minOccurs="0" />
			<xs:element name="billTo" type="anet:customerAddressType" minOccurs="0"/>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerPaymentProfileType">
		<xs:complexContent>
			<xs:extension base="anet:customerPaymentProfileBaseType">
				<xs:sequence>
					<xs:element name="payment" type="anet:paymentSimpleType" minOccurs="0"/>
					<xs:element name="driversLicense" type="anet:driversLicenseType" minOccurs="0"/>
					<xs:element name="taxId" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="anet:numericString">
								<xs:minLength value="9" />
								<xs:maxLength value="9" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerPaymentProfileExType">
		<xs:complexContent>
			<xs:extension base="anet:customerPaymentProfileType">
				<xs:sequence>
					<xs:element name="customerPaymentProfileId" type="anet:numericString" minOccurs="0" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerPaymentProfileMaskedType">
		<xs:complexContent>
			<xs:extension base="anet:customerPaymentProfileBaseType">
				<xs:sequence>
					<xs:element name="customerPaymentProfileId" type="anet:numericString" minOccurs="0" />
					<xs:element name="payment" type="anet:paymentMaskedType" minOccurs="0"/>
					<xs:element name="driversLicense" type="anet:driversLicenseMaskedType" minOccurs="0"/>
					<xs:element name="taxId" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:length value="8" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerProfileBaseType">
		<xs:sequence>
			<xs:element name="merchantCustomerId" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="description" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="email" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerProfileType">
		<xs:complexContent>
			<xs:extension base="anet:customerProfileBaseType">
				<xs:sequence>
					<xs:element name="paymentProfiles" type="anet:customerPaymentProfileType" minOccurs="0" maxOccurs="unbounded" />
					<xs:element name="shipToList" type="anet:customerAddressType" minOccurs="0" maxOccurs="unbounded" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerProfileExType">
		<xs:complexContent>
			<xs:extension base="anet:customerProfileBaseType">
				<xs:sequence>
					<xs:element name="customerProfileId" type="anet:numericString" minOccurs="0" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerProfileMaskedType">
		<xs:complexContent>
			<xs:extension base="anet:customerProfileExType">
				<xs:sequence>
					<xs:element name="paymentProfiles" type="anet:customerPaymentProfileMaskedType" minOccurs="0" maxOccurs="unbounded" />
					<xs:element name="shipToList" type="anet:customerAddressExType" minOccurs="0" maxOccurs="unbounded" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerAddressType">
		<xs:complexContent>
			<xs:extension base="anet:nameAndAddressType">
				<xs:sequence>
					<xs:element name="phoneNumber" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:maxLength value="255" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<xs:element name="faxNumber" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:maxLength value="255" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="customerAddressExType">
		<xs:complexContent>
			<xs:extension base="anet:customerAddressType">
				<xs:sequence>
					<xs:element name="customerAddressId" type="anet:numericString" minOccurs="0" />
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="extendedAmountType">
		<xs:sequence>
			<xs:element name="amount">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.00" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="name" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="31" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="description" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="lineItemType">
		<xs:sequence>
			<xs:element name="itemId">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="1" />
						<xs:maxLength value="31" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="name">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:minLength value="1" />
						<xs:maxLength value="31" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="description" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="255" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="quantity">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.00" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="unitPrice">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.00" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="taxable" type="xs:boolean" minOccurs="0" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransAmountType">
		<xs:sequence>
			<xs:element name="amount">
				<xs:simpleType>
					<xs:restriction base="xs:decimal">
						<xs:minInclusive value="0.01" />
						<xs:fractionDigits value="4" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
			<xs:element name="tax" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="shipping" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="duty" type="anet:extendedAmountType" minOccurs="0" />
			<xs:element name="lineItems" type="anet:lineItemType" minOccurs="0" maxOccurs="30" />
		</xs:sequence>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransOrderType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransAmountType">
				<xs:sequence>
					<xs:element name="customerProfileId" type="anet:numericString" />
					<xs:element name="customerPaymentProfileId" type="anet:numericString" />
					<xs:element name="customerShippingAddressId" type="anet:numericString" minOccurs="0" />
					<xs:element name="order" type="anet:orderExType" minOccurs="0" />
					<xs:element name="taxExempt" type="xs:boolean" minOccurs="0" />
					<xs:element name="recurringBilling" type="xs:boolean" minOccurs="0" />
					<xs:element name="cardCode" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="anet:numericString">
								<xs:minLength value="3" />
								<xs:maxLength value="4" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransAuthCaptureType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransOrderType">
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransAuthOnlyType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransOrderType">
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransCaptureOnlyType">
		<xs:complexContent>
			<xs:extension base="anet:profileTransOrderType">
				<xs:sequence>
					<xs:element name="approvalCode">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:maxLength value="6" />
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
				</xs:sequence>
			</xs:extension>
		</xs:complexContent>
	</xs:complexType>
	<!-- ===================================================== -->
	<xs:complexType name="profileTransactionType">
		<xs:choice>
			<xs:element name="profileTransAuthCapture" type="anet:profileTransAuthCaptureType" />
			<xs:element name="profileTransAuthOnly" type="anet:profileTransAuthOnlyType" />
			<xs:element name="profileTransCaptureOnly" type="anet:profileTransCaptureOnlyType" />
		</xs:choice>
	</xs:complexType>
	<!-- 
	=================================================================== 
	The ANetApiRequest defines elements common to all API method
	requests.
	=================================================================== 
	-->
	<xs:complexType name="ANetApiRequest">
		<xs:sequence>
			<xs:element name="merchantAuthentication" type="anet:merchantAuthenticationType" />
			<xs:element name="refId" minOccurs="0">
				<xs:simpleType>
					<xs:restriction base="xs:string">
						<xs:maxLength value="20" />
					</xs:restriction>
				</xs:simpleType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- 
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	 Response type definitions begin here
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	-->
	<!-- 
	===================================================================
	The messagesType provides the result of the request. The resultCode
	element provides the overall result of the request. The individual
	message(s) provide more detail, especially for errors, about the result.
	
	Ok	  - The request was processed and accepted without error. If any
			  messages are present they will be informational only.
	Error   - The request resulted in one or more errors. See messages
			  for details.
	===================================================================
	-->
	<xs:simpleType name="messageTypeEnum">
		<xs:restriction base="xs:string">
			<xs:enumeration value="Ok" />
			<xs:enumeration value="Error" />
		</xs:restriction>
	</xs:simpleType>
	<xs:complexType name="messagesType">
		<xs:sequence>
			<xs:element name="resultCode" type="anet:messageTypeEnum" />
			<xs:element name="message" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="code" type="xs:string" />
						<xs:element name="text" type="xs:string" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<!-- 
	===================================================================
	The ANetApiResponse defines elements common to all API method 
	responses.
	===================================================================
	-->
	<xs:complexType name="ANetApiResponse">
		<xs:sequence>
			<xs:element name="refId" type="xs:string" minOccurs="0" />
			<xs:sequence>
				<xs:element name="messages" type="anet:messagesType" />
			</xs:sequence>
		</xs:sequence>
	</xs:complexType>
	<!-- 
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	 API method definitions begin here		 
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	-->
	<!-- 
	===================================================================
	errorResponse
	This is the response when an error occurs before the method can
	be determined, such as an "unknown method" type of error.
	===================================================================
	-->
	<xs:element name="ErrorResponse" type="anet:ANetApiResponse" />
	<!-- 
	===================================================================
	isAliveRequest
	This method is used to test the availability of the API.
	===================================================================
	-->
	<xs:element name="isAliveRequest">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="refId" minOccurs="0">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:maxLength value="20" />
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	isAliveResponse
	This is the response to isAliveRequest.
	===================================================================
	-->
	<xs:element name="isAliveResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	authenticateTestRequest
	This method is used to test the availability of the API.
	===================================================================
	-->
	<xs:element name="authenticateTestRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	authenticateTestResponse
	This is the response to authenticateTestRequest.
	===================================================================
	-->
	<xs:element name="authenticateTestResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	ARBCreateSubscriptionRequest
	This method is used to create a new ARB subscription.
	===================================================================
	-->
	<xs:element name="ARBCreateSubscriptionRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="subscription" type="anet:ARBSubscriptionType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	ARBCreateSubscriptionResponse
	This is the response to ARBCreateSubscriptionRequest.
	===================================================================
	-->
	<xs:element name="ARBCreateSubscriptionResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- subscriptionId will only be present if a subscription was created. -->
						<xs:element name="subscriptionId" type="anet:numericString" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	ARBUpdateSubscriptionRequest
	This method is used to update an existing ARB subscription.
	===================================================================
	-->
	<xs:element name="ARBUpdateSubscriptionRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="subscriptionId" type="anet:numericString" />
						<xs:element name="subscription" type="anet:ARBSubscriptionType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	ARBUpdateSubscriptionResponse
	This is the response to ARBUpdateSubscriptionResponse.
	===================================================================
	-->
	<xs:element name="ARBUpdateSubscriptionResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	ARBCancelSubscriptionRequest
	This method is used to cancel an existing ARB subscription.
	===================================================================
	-->
	<xs:element name="ARBCancelSubscriptionRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="subscriptionId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	ARBCancelSubscriptionResponse
	This is the response to ARBCancelSubscriptionRequest.
	===================================================================
	-->
	<xs:element name="ARBCancelSubscriptionResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	createCustomerProfileRequest
	This method is used to create a new customer profile along with any 
	customer payment profiles and customer shipping addresses for the customer profile.
	===================================================================
	-->
	<xs:element name="createCustomerProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="profile" type="anet:customerProfileType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	createCustomerProfileResponse
	This is the response to createCustomerProfileRequest.
	===================================================================
	-->
	<xs:element name="createCustomerProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- customerProfileId will only be present if a profile was created. -->
						<xs:element name="customerProfileId" type="anet:numericString" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	createCustomerPaymentProfileRequest
	This method is used to create a new customer payment profile for an existing customer profile.
	===================================================================
	-->
	<xs:element name="createCustomerPaymentProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="paymentProfile" type="anet:customerPaymentProfileType" />
						<xs:element name="validationMode" type="anet:validationModeEnum" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	createCustomerPaymentProfileResponse
	This is the response to createCustomerPaymentProfileRequest.
	===================================================================
	-->
	<xs:element name="createCustomerPaymentProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- customerPaymentProfileId will only be present if a payment profile was created. -->
						<xs:element name="customerPaymentProfileId" type="anet:numericString" minOccurs="0" />
						<!-- validationDirectResponse will only be present if validationMode is testMode or liveMode. -->
						<xs:element name="validationDirectResponse" minOccurs="0" >
							<xs:simpleType>
								<xs:restriction base="xs:string">
									<xs:maxLength value="2048" />
								</xs:restriction>
							</xs:simpleType>
						</xs:element>
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	createCustomerShippingAddressRequest
	This method is used to create a new customer shipping address for an existing customer profile.
	===================================================================
	-->
	<xs:element name="createCustomerShippingAddressRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="address" type="anet:customerAddressType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	createCustomerShippingAddressResponse
	This is the response to createCustomerShippingAddressRequest.
	===================================================================
	-->
	<xs:element name="createCustomerShippingAddressResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- customerAddressId will only be present if a payment profile was created. -->
						<xs:element name="customerAddressId" type="anet:numericString" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	getCustomerProfileRequest
	This method is used to retrieve an existing customer profile along with all the 
	customer payment profiles and customer shipping addresses for the customer profile.
	===================================================================
	-->
	<xs:element name="getCustomerProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	getCustomerProfileResponse
	This is the response to getCustomerProfileRequest.
	===================================================================
	-->
	<xs:element name="getCustomerProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- profile will only be present if a profile was successfully retrieved. -->
						<xs:element name="profile" type="anet:customerProfileMaskedType" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	getCustomerPaymentProfileRequest
	This method is used to retrieve an existing customer payment profile for a customer profile.
	===================================================================
	-->
	<xs:element name="getCustomerPaymentProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="customerPaymentProfileId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	getCustomerPaymentProfileResponse
	This is the response to getCustomerPaymentProfileRequest.
	===================================================================
	-->
	<xs:element name="getCustomerPaymentProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- paymentProfile and customerProfileId will only be present if a payment profile was successfully retrieved. -->
						<xs:element name="paymentProfile" type="anet:customerPaymentProfileMaskedType" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	getCustomerShippingAddressRequest
	This method is used to retrieve an existing customer shipping address for a customer profile.
	===================================================================
	-->
	<xs:element name="getCustomerShippingAddressRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="customerAddressId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	getCustomerShippingAddressResponse
	This is the response to getCustomerShippingAddressRequest.
	===================================================================
	-->
	<xs:element name="getCustomerShippingAddressResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<!-- address and customerProfileId will only be present if a shipping address was successfully retrieved. -->
						<xs:element name="address" type="anet:customerAddressExType" minOccurs="0" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	updateCustomerProfileRequest
	This method is used to update an existing customer profile.
	===================================================================
	-->
	<xs:element name="updateCustomerProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="profile" type="anet:customerProfileExType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	updateCustomerProfileResponse
	This is the response to updateCustomerProfileRequest.
	===================================================================
	-->
	<xs:element name="updateCustomerProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	updateCustomerPaymentProfileRequest
	This method is used to update an existing customer payment profile for a customer profile.
	===================================================================
	-->
	<xs:element name="updateCustomerPaymentProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="paymentProfile" type="anet:customerPaymentProfileExType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	updateCustomerPaymentProfileResponse
	This is the response to updateCustomerPaymentProfileRequest.
	===================================================================
	-->
	<xs:element name="updateCustomerPaymentProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	updateCustomerShippingAddressRequest
	This method is used to update an existing customer shipping address for a customer profile.
	===================================================================
	-->
	<xs:element name="updateCustomerShippingAddressRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="address" type="anet:customerAddressExType" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	updateCustomerShippingAddressResponse
	This is the response to updateCustomerShippingAddressRequest.
	===================================================================
	-->
	<xs:element name="updateCustomerShippingAddressResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	deleteCustomerProfileRequest
	This method is used to delete an existing customer profile along with all the 
	customer payment profiles and customer shipping addresses for the customer profile.
	===================================================================
	-->
	<xs:element name="deleteCustomerProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	deleteCustomerProfileResponse
	This is the response to deleteCustomerProfileRequest.
	===================================================================
	-->
	<xs:element name="deleteCustomerProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	deleteCustomerPaymentProfileRequest
	This method is used to delete an existing customer payment profile from a customer profile.
	===================================================================
	-->
	<xs:element name="deleteCustomerPaymentProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="customerPaymentProfileId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	deleteCustomerPaymentProfileResponse
	This is the response to deleteCustomerPaymentProfileRequest.
	===================================================================
	-->
	<xs:element name="deleteCustomerPaymentProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	deleteCustomerShippingAddressRequest
	This method is used to delete an existing customer shipping address from a customer profile.
	===================================================================
	-->
	<xs:element name="deleteCustomerShippingAddressRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="customerAddressId" type="anet:numericString" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	deleteCustomerShippingAddressResponse
	This is the response to deleteCustomerShippingAddressRequest.
	===================================================================
	-->
	<xs:element name="deleteCustomerShippingAddressResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	createCustomerProfileTransactionRequest
	This method is used to generate a payment transaction for a customer payment profile.
	===================================================================
	-->
	<xs:element name="createCustomerProfileTransactionRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="transaction" type="anet:profileTransactionType" />
						<xs:element name="extraOptions" minOccurs="0">
							<xs:simpleType>
								<xs:restriction base="xs:string">
									<xs:maxLength value="1024" />
								</xs:restriction>
							</xs:simpleType>
						</xs:element>
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	createCustomerProfileTransactionResponse
	This is the response to createCustomerProfileTransactionRequest.
	===================================================================
	-->
	<xs:element name="createCustomerProfileTransactionResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="directResponse" minOccurs="0" >
							<xs:simpleType>
								<xs:restriction base="xs:string">
									<xs:maxLength value="2048" />
								</xs:restriction>
							</xs:simpleType>
						</xs:element>
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	validateCustomerPaymentProfileRequest
	This method is used to check a customer payment profile by generating a test transaction for it.
	===================================================================
	-->
	<xs:element name="validateCustomerPaymentProfileRequest">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiRequest">
					<xs:sequence>
						<xs:element name="customerProfileId" type="anet:numericString" />
						<xs:element name="customerPaymentProfileId" type="anet:numericString" />
						<xs:element name="customerShippingAddressId" type="anet:numericString" minOccurs="0" />
						<xs:element name="validationMode" type="anet:validationModeEnum" />
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
	<!-- 
	===================================================================
	validateCustomerPaymentProfileResponse
	This is the response to validateCustomerPaymentProfileRequest.
	===================================================================
	-->
	<xs:element name="validateCustomerPaymentProfileResponse">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="anet:ANetApiResponse">
					<xs:sequence>
						<xs:element name="directResponse" minOccurs="0" >
							<xs:simpleType>
								<xs:restriction base="xs:string">
									<xs:maxLength value="2048" />
								</xs:restriction>
							</xs:simpleType>
						</xs:element>
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
</xs:schema>

"""