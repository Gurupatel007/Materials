<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="Project_guru.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <table runat="server">
                <tr runat="server">
                    <td runat="server">
                        <asp:Label ID="Label1" runat="server" Text="Username" ></asp:Label>
                    </td>
                    <td runat="server">
                         <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ErrorMessage="Name cannot be blank" ControlToValidate="TextBox1" ForeColor="Red"></asp:RequiredFieldValidator> 
                    </td>
                </tr>
                <tr runat="server">
                    <td runat="server">
                        <asp:Label ID="Label7" runat="server" Text="Email"></asp:Label>
                    </td>
                    <td runat="server">
                        <asp:TextBox ID="TextBox2" runat="server"  ></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ErrorMessage="Email cannot be blank" ControlToValidate="TextBox2" ForeColor="Red"></asp:RequiredFieldValidator>
                        <asp:RegularExpressionValidator ID="RegularExpressionValidator1" runat="server" ControlToValidate="TextBox2" ErrorMessage="Enter proper email format" ForeColor="Red" ValidationExpression="\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*"></asp:RegularExpressionValidator> 
                    </td>
                </tr>
                <tr runat="server">
                    <td runat="server">
                        <asp:Label ID="Label8" runat="server" Text="Mobile No."></asp:Label>
                    </td>
                    <td runat="server">
                        <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator3" runat="server" ErrorMessage="Mobile cannot be blank" ControlToValidate="TextBox3" ForeColor="Red"></asp:RequiredFieldValidator>  
           <asp:RegularExpressionValidator ID="RegularExpressionValidator2" runat="server" ControlToValidate="TextBox3" ErrorMessage="Mobile number must be 10 digit" ForeColor="Red" ValidationExpression="\d{10}"></asp:RegularExpressionValidator> 
                    </td>
                </tr>
                <tr runat="server">
                    <td runat="server">
                        <asp:Label ID="Label2" runat="server" Text="Password"></asp:Label>
                    </td>
                    <td runat="server">
                        <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator4" runat="server" ErrorMessage="Password cannot be blank" ControlToValidate="TextBox4" ForeColor="Red"></asp:RequiredFieldValidator>
                    </td>
                </tr>
                <tr runat="server">
                    <td runat="server">
                        <asp:Label ID="Label3" runat="server" Text="DateofBirth"></asp:Label>
                    </td>
                    <td runat="server">
                        <asp:TextBox ID="TextBox5" runat="server"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator5" runat="server" ErrorMessage="Required" ControlToValidate="TextBox5"></asp:RequiredFieldValidator>
                    </td>
                </tr>
                <tr runat="server">
                    <td runat="server">
                        <asp:Label ID="Label4" runat="server" Text="Address"></asp:Label>
                    </td>
                    <td runat="server">
                        <asp:TextBox ID="TextBox6" runat="server"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator6" runat="server" ErrorMessage="Required" ControlToValidate="TextBox6"></asp:RequiredFieldValidator>
                    </td>
                </tr>
                <tr runat="server">
                    <td runat="server">
                        <asp:Label ID="Label5" runat="server" Text="Country "></asp:Label>
                    </td>
                    <td runat="server">
                        <asp:TextBox ID="TextBox7" runat="server"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator7" runat="server" ErrorMessage="Required" ControlToValidate="TextBox7"></asp:RequiredFieldValidator>
                    </td>
                </tr>
                <tr runat="server">
                    <td runat="server">
                        <asp:Label ID="Label6" runat="server" Text="State   "></asp:Label>
                    </td>
                    <td runat="server">
                        <asp:TextBox ID="TextBox8" runat="server"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator8" runat="server" ErrorMessage="Required" ControlToValidate="TextBox8"></asp:RequiredFieldValidator>
                    </td>
                </tr>
                <tr runat="server">
                    <td runat="server">
                        
                    </td>
                    <td runat="server">
                        <asp:Button ID="Button2" runat="server" Text="Submit" OnClick="Button2_Click" />
                    </td>
                </tr>
            </table>
        </div>
    </form>
</body>
</html>
