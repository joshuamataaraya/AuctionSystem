USE [AuctionSystem]
GO
/****** Object:  UserDefinedDataType [dbo].[Alias]    Script Date: 14/05/2015 07:58:41 p.m. ******/
CREATE TYPE [dbo].[Alias] FROM [varchar](15) NULL
GO
/****** Object:  UserDefinedDataType [dbo].[Colones]    Script Date: 14/05/2015 07:58:41 p.m. ******/
CREATE TYPE [dbo].[Colones] FROM [bigint] NOT NULL
GO
/****** Object:  UserDefinedDataType [dbo].[Telefono]    Script Date: 14/05/2015 07:58:41 p.m. ******/
CREATE TYPE [dbo].[Telefono] FROM [varchar](11) NULL
GO
/****** Object:  Table [dbo].[CategoriaPrimaria]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[CategoriaPrimaria](
	[Id] [int] NOT NULL,
	[Nombre] [varchar](50) NOT NULL,
 CONSTRAINT [PK_CategoriaPrimaria] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[CategoriaSecundaria]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[CategoriaSecundaria](
	[Id] [int] NOT NULL,
	[Nombre] [varchar](50) NOT NULL,
 CONSTRAINT [PK_CategoriaSecundaria] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Comentario]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Comentario](
	[Id] [int] NOT NULL,
	[Texto] [varchar](max) NOT NULL,
	[IdSubasta] [int] NULL,
 CONSTRAINT [PK_Comentario] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[DetallesDeEntrega]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[DetallesDeEntrega](
	[Id] [int] NOT NULL,
	[Lugar] [varchar](50) NOT NULL,
	[Especificación] [varchar](50) NULL,
 CONSTRAINT [PK_DetallesDeEntrega] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Item]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Item](
	[Id] [int] NOT NULL,
	[Descripcion] [varchar](50) NOT NULL,
	[Foto] [image] NULL,
	[idCategoriaPrimaria] [int] NOT NULL,
	[idCategoriaSecundaria] [int] NOT NULL,
 CONSTRAINT [PK_Item] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[itemsXSubasta]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[itemsXSubasta](
	[Id] [int] NOT NULL,
	[IdItem] [int] NOT NULL,
	[IdSubasta] [int] NOT NULL,
 CONSTRAINT [PK_itemsXSubasta] PRIMARY KEY CLUSTERED 
(
	[Id] ASC,
	[IdItem] ASC,
	[IdSubasta] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Nombre]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Nombre](
	[Alias] [dbo].[Alias] NOT NULL,
	[Nombre] [varchar](50) NOT NULL,
	[Apellido] [varchar](50) NOT NULL,
 CONSTRAINT [PK_Nombre] PRIMARY KEY CLUSTERED 
(
	[Alias] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[ParámetrosDelSystema]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ParámetrosDelSystema](
	[Id] [int] NOT NULL,
	[MontoMinimoDeOferta] [bigint] NOT NULL,
	[MontoPorSubastar] [bigint] NOT NULL,
 CONSTRAINT [PK_ParámetrosDelSystema] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Partcipante]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Partcipante](
	[Alias] [dbo].[Alias] NOT NULL,
	[Email] [varchar](50) NOT NULL,
	[EstaSuspendido] [bit] NOT NULL,
	[IdVendedor] [bit] NULL,
	[Tarjeta] [int] NULL,
 CONSTRAINT [PK_Partcipante] PRIMARY KEY CLUSTERED 
(
	[Alias] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Pujas]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Pujas](
	[Id] [int] NOT NULL,
	[AliasComprador] [dbo].[Alias] NOT NULL,
	[IdSubasta] [int] NOT NULL,
	[Monto] [dbo].[Colones] NOT NULL,
	[Momento] [datetime] NOT NULL,
 CONSTRAINT [PK_Pujas] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Subasta]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Subasta](
	[Id] [int] NOT NULL,
	[LímiteCierre] [datetime] NOT NULL,
	[AliasVendedor] [dbo].[Alias] NOT NULL,
	[EstaCerrada] [bit] NOT NULL,
	[AliasComprador] [dbo].[Alias] NULL,
	[IDUltimaPuja] [int] NULL,
 CONSTRAINT [PK_Subasta] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Telefono]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Telefono](
	[Alias] [dbo].[Alias] NOT NULL,
	[idUsuario] [int] NOT NULL,
	[Numero] [dbo].[Telefono] NOT NULL,
 CONSTRAINT [PK_Telefono] PRIMARY KEY CLUSTERED 
(
	[Alias] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Usuario]    Script Date: 14/05/2015 07:58:41 p.m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Usuario](
	[Alias] [dbo].[Alias] NOT NULL,
	[Password] [int] NOT NULL,
	[Direccion] [varchar](50) NOT NULL,
	[Cedula] [int] NULL,
	[idNombre] [int] NOT NULL,
	[esParticipante] [bit] NOT NULL,
	[esAdministrador] [bit] NOT NULL,
 CONSTRAINT [PK_Usuario_1] PRIMARY KEY CLUSTERED 
(
	[Alias] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
ALTER TABLE [dbo].[Comentario]  WITH CHECK ADD  CONSTRAINT [FK_Comentario_Subasta] FOREIGN KEY([IdSubasta])
REFERENCES [dbo].[Subasta] ([Id])
GO
ALTER TABLE [dbo].[Comentario] CHECK CONSTRAINT [FK_Comentario_Subasta]
GO
ALTER TABLE [dbo].[DetallesDeEntrega]  WITH CHECK ADD  CONSTRAINT [FK_DetallesDeEntrega_Subasta] FOREIGN KEY([Id])
REFERENCES [dbo].[Subasta] ([Id])
GO
ALTER TABLE [dbo].[DetallesDeEntrega] CHECK CONSTRAINT [FK_DetallesDeEntrega_Subasta]
GO
ALTER TABLE [dbo].[Item]  WITH CHECK ADD  CONSTRAINT [FK_Item_CategoriaPrimaria] FOREIGN KEY([idCategoriaPrimaria])
REFERENCES [dbo].[CategoriaPrimaria] ([Id])
GO
ALTER TABLE [dbo].[Item] CHECK CONSTRAINT [FK_Item_CategoriaPrimaria]
GO
ALTER TABLE [dbo].[Item]  WITH CHECK ADD  CONSTRAINT [FK_Item_CategoriaSecundaria] FOREIGN KEY([idCategoriaSecundaria])
REFERENCES [dbo].[CategoriaSecundaria] ([Id])
GO
ALTER TABLE [dbo].[Item] CHECK CONSTRAINT [FK_Item_CategoriaSecundaria]
GO
ALTER TABLE [dbo].[itemsXSubasta]  WITH CHECK ADD  CONSTRAINT [FK_itemsXSubasta_Item] FOREIGN KEY([IdItem])
REFERENCES [dbo].[Item] ([Id])
GO
ALTER TABLE [dbo].[itemsXSubasta] CHECK CONSTRAINT [FK_itemsXSubasta_Item]
GO
ALTER TABLE [dbo].[itemsXSubasta]  WITH CHECK ADD  CONSTRAINT [FK_itemsXSubasta_Subasta] FOREIGN KEY([IdSubasta])
REFERENCES [dbo].[Subasta] ([Id])
GO
ALTER TABLE [dbo].[itemsXSubasta] CHECK CONSTRAINT [FK_itemsXSubasta_Subasta]
GO
ALTER TABLE [dbo].[Nombre]  WITH CHECK ADD  CONSTRAINT [FK_Nombre_Usuario] FOREIGN KEY([Alias])
REFERENCES [dbo].[Usuario] ([Alias])
GO
ALTER TABLE [dbo].[Nombre] CHECK CONSTRAINT [FK_Nombre_Usuario]
GO
ALTER TABLE [dbo].[Partcipante]  WITH CHECK ADD  CONSTRAINT [FK_Partcipante_Usuario] FOREIGN KEY([Alias])
REFERENCES [dbo].[Usuario] ([Alias])
GO
ALTER TABLE [dbo].[Partcipante] CHECK CONSTRAINT [FK_Partcipante_Usuario]
GO
ALTER TABLE [dbo].[Pujas]  WITH CHECK ADD  CONSTRAINT [FK_Pujas_Partcipante] FOREIGN KEY([AliasComprador])
REFERENCES [dbo].[Partcipante] ([Alias])
GO
ALTER TABLE [dbo].[Pujas] CHECK CONSTRAINT [FK_Pujas_Partcipante]
GO
ALTER TABLE [dbo].[Pujas]  WITH CHECK ADD  CONSTRAINT [FK_Pujas_Subasta] FOREIGN KEY([IdSubasta])
REFERENCES [dbo].[Subasta] ([Id])
GO
ALTER TABLE [dbo].[Pujas] CHECK CONSTRAINT [FK_Pujas_Subasta]
GO
ALTER TABLE [dbo].[Subasta]  WITH CHECK ADD  CONSTRAINT [FK_Subasta_Partcipante] FOREIGN KEY([AliasVendedor])
REFERENCES [dbo].[Partcipante] ([Alias])
GO
ALTER TABLE [dbo].[Subasta] CHECK CONSTRAINT [FK_Subasta_Partcipante]
GO
ALTER TABLE [dbo].[Subasta]  WITH CHECK ADD  CONSTRAINT [FK_Subasta_Partcipante1] FOREIGN KEY([AliasComprador])
REFERENCES [dbo].[Partcipante] ([Alias])
GO
ALTER TABLE [dbo].[Subasta] CHECK CONSTRAINT [FK_Subasta_Partcipante1]
GO
ALTER TABLE [dbo].[Subasta]  WITH CHECK ADD  CONSTRAINT [FK_Subasta_Pujas] FOREIGN KEY([IDUltimaPuja])
REFERENCES [dbo].[Pujas] ([Id])
GO
ALTER TABLE [dbo].[Subasta] CHECK CONSTRAINT [FK_Subasta_Pujas]
GO
ALTER TABLE [dbo].[Telefono]  WITH CHECK ADD  CONSTRAINT [FK_Telefono_Usuario] FOREIGN KEY([Alias])
REFERENCES [dbo].[Usuario] ([Alias])
GO
ALTER TABLE [dbo].[Telefono] CHECK CONSTRAINT [FK_Telefono_Usuario]
GO
