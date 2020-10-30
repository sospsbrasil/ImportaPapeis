import os
import urllib
import urllib.request
from bs4 import BeautifulSoup as fsoup

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = fsoup(thepage, 'lxml')
    return soupdata

playerdatasaved = ""
playerdata = ""
array = ["AALR3","ABCB3","ABCB4","ABEV3","ABRE3","ABYA3","ACES3","ACES4","ADHM3","AEDU11","AEDU3","AELP3","AESL3","AESL4","AFLT3","AFLU3","AFLU5","AGEI3","AGEN33","AGIN3","AGRO3","AHEB3","AHEB5","AHEB6","ALBA3","ALLL11","ALLL3","ALLL4","ALPA3","ALPA4","ALSC3","ALSO3","ALUP11","ALUP3","ALUP4","AMAR3","AMBV3","AMBV4","AMIL3","AMPI3","ANIM3","AORE3","APER3","APTI4","ARCE3","ARCZ3","ARCZ6","ARLA3","ARLA4","ARPS3","ARPS4","ARTE3","ARTE4","ARTR3","ARZZ3","ASSM3","ASSM4","ASTA4","ATOM3","AUTM3","AVIL3","AZEV3","AZEV4","AZUL4","B3SA3","BAHI11","BAHI3","BAHI4","BAHI5","BALM3","BALM4","BAUH4","BAZA3","BBAS3","BBDC3","BBDC4","BBRK3","BBSE3","BBTG11","BBTG12","BBTG13","BCAL6","BDLL3","BDLL4","BECE3","BECE4","BEEF3","BEES3","BEES4","BELG3","BELG4","BEMA3","BERG3","BESP3","BESP4","BFIT3","BFIT4","BGIP3","BGIP4","BHGR3","BICB3","BICB4","BIDI11","BIDI3","BIDI4","BIOM3","BIOM4","BISA3","BKBR3","BMEB3","BMEB4","BMEF3","BMGB11","BMGB4","BMIN3","BMIN4","BMKS3","BMTO3","BMTO4","BNBR3","BNBR4","BNCA3","BOBR3","BOBR4","BOVH3","BPAC11","BPAC3","BPAC5","BPAN4","BPAR3","BPAT33","BPHA3","BPIA3","BPNM3","BPNM4","BRAP3","BRAP4","BRDT3","BRFS3","BRGE11","BRGE12","BRGE3","BRGE5","BRGE6","BRGE7","BRGE8","BRIN3","BRIV3","BRIV4","BRKM3","BRKM5","BRKM6","BRML3","BRPR3","BRSR3","BRSR4","BRSR5","BRSR6","BRTP3","BRTP4","BSCT3","BSCT5","BSCT6","BSEV3","BSGR3","BSLI3","BSLI4","BTOW3","BTTL3","BTTL4","BUET3","BUET4","BVMF3","CAFE3","CAFE4","CALI3","CALI4","CAMB3","CAMB4","CAML3","CARD3","CASN3","CBEE3","CBMA3","CBMA4","CCHI3","CCHI4","CCIM3","CCPR3","CCRO3","CCTU4","CCXC3","CEAB3","CEBR3","CEBR5","CEBR6","CEDO3","CEDO4","CEEB3","CEEB5","CEED3","CEED4","CEGR3","CELM3","CELP5","CELP7","CEPE3","CEPE5","CEPE6","CESP3","CESP4","CESP5","CESP6","CFLU4","CGAS3","CGAS5","CGOS3","CGOS4","CGRA3","CGRA4","CIEL3","CIQU3","CIQU4","CLAN3","CLAN4","CLSC3","CLSC4","CLSC5","CLSC6","CMET4","CMIG3","CMIG4","CMMA4","CNFB4","CNTO3","COCE3","COCE5","COCE6","COGN3","CORR3","CORR4","CPFE3","CPFG3","CPFG4","CPFP4","CPLE3","CPLE5","CPLE6","CPNY3","CPRE3","CPSL3","CRBM3","CRBM7","CRDE3","CREM3","CREM4","CRFB3","CRIV3","CRIV4","CRPG3","CRPG5","CRPG6","CRTP3","CRTP5","CRUZ3","CSAB3","CSAB4","CSAN3","CSMG3","CSNA3","CSPC3","CSPC4","CSRN3","CSRN5","CSRN6","CSTB3","CSTB4","CTIP3","CTKA3","CTKA4","CTNM3","CTNM4","CTPC3","CTPC4","CTSA3","CTSA4","CTSA8","CTWR3","CVCB3","CYRE3","CYRE4","CZLT33","CZRS3","CZRS4","DAGB33","DASA3","DAYC3","DAYC4","DFVA3","DFVA4","DHBI3","DHBI4","DIRR3","DJON4","DMMO3","DOCA3","DOCA4","DOHL3","DOHL4","DPPI3","DPPI4","DSUL3","DTCY3","DTEX3","DUFB11","DUQE3","DUQE4","DURA3","DURA4","DXTG4","EALT3","EALT4","EBCO3","EBCO4","EBEN4","EBTP3","EBTP4","ECIS3","ECIS4","ECOR3","ECPR3","ECPR4","EEEL3","EEEL4","EGIE3","EKTR3","EKTR4","ELCA3","ELCA4","ELEK3","ELEK4","ELET3","ELET5","ELET6","ELEV3","ELPL3","ELPL4","ELPL5","ELPL6","ELUM3","ELUM4","EMAE4","EMBR3","ENAT3","ENBR3","ENER3","ENER5","ENER6","ENEV3","ENGI11","ENGI3","ENGI4","ENMT3","ENMT4","EQPA3","EQPA5","EQPA6","EQPA7","EQTL3","ESCE3","ESTC11","ESTC3","ESTC4","ESTR3","ESTR4","ETER3","ETER4","EUCA3","EUCA4","EVEN3","EZTC3","FBMC3","FBMC4","FBRA4","FCAP3","FCAP4","FESA3","FESA4","FFTL3","FFTL4","FGUI3","FGUI4","FHER3","FIBR3","FIGE3","FIGE4","FJTA3","FJTA4","FLCL3","FLCL5","FLCL6","FLRY3","FRAS3","FRAS4","FRIO3","FRTA3","FTRX3","FTRX4","GAFP3","GAFP4","GALO3","GALO4","GAZO3","GAZO4","GBIO33","GEPA3","GEPA4","GETI3","GETI4","GFSA3","GGBR3","GGBR4","GLOB4","GNDI3","GOAU3","GOAU4","GOLL4","GPCP3","GPIV33","GRND3","GRNL4","GSHP3","GUAR3","GUAR4","GVTT3","HAGA3","HAGA4","HAPV3","HBOR3","HBTS5","HETA3","HETA4","HGTX3","HGTX4","HOOT4","HRTP3","HYPE3","ICPI3","IDNT3","IDVL11","IDVL3","IDVL4","IENG3","IENG5","IGBR3","IGBR5","IGBR6","IGTA3","IGUA3","IGUA5","IGUA6","ILLS4","ILMD3","ILMD4","IMBI3","IMBI4","IMCH3","INEP3","INEP4","INET3","INHA3","IRBR3","ITEC3","ITSA3","ITSA4","ITUB3","ITUB4","IVTT3","JBDU3","JBDU4","JBSS3","JFAB4","JFEN3","JHSF3","JOPA3","JOPA4","JPSA3","JSLG3","KEPL3","KLBN11","KLBN3","KLBN4","KROT11","KROT3","KROT4","KSSA3","LAME3","LAME4","LATM11","LATS3","LCAM3","LCSA3","LCSA4","LECO3","LECO4","LETO3","LETO5","LEVE3","LEVE4","LFFE3","LFFE4","LGLO4","LIGH3","LIGT3","LINX3","LIPR3","LIQO3","LIXC3","LIXC4","LLIS3","LOGG3","LOGN3","LPSB3","LREN3","LREN4","LUPA3","LUXM3","LUXM4","LWSA3","MAGG3","MAGS3","MAPT3","MAPT4","MARI3","MDIA3","MDNE3","MEAL3","MEDI3","MEND5","MEND6","MERC3","MERC4","MGEL3","MGEL4","MGLU3","MILK33","MILS3","MLFT3","MLFT4","MLPA12","MLPA3","MLPA4","MMAQ3","MMAQ4","MMXM3","MNDL3","MNDL4","MNPR3","MNPR4","MNSA3","MNSA4","MOAR3","MOVI3 ","MPLU3","MRFG3","MRSL3","MRSL4","MRVE3","MSAN3","MSAN4","MSPA3","MSPA4","MTBR3","MTBR4","MTIG3","MTIG4","MTRE3","MTSA4","MULT3","MWET3","MWET4","MYPK3","MYPK4","NAFG3","NAFG4","NATU3","NEOE3","NETC3","NETC4","NORD3","NTCO3","NUTR3","ODPV3","OFSA3","OGXP3","OIBR3","OIBR4","OMGE3","OSAO4","OSXB3","PALF11","PALF3","PALF5","PARC3","PARD3","PATI3","PATI4","PCAR3","PCAR4","PCAR5","PDGR3","PEAB3","PEAB4","PEFX3","PEFX5","PETR3","PETR4","PFRM3","PINE3","PINE4","PITI4","PLAS3","PLDN4","PLIM4","PLTO5","PLTO6","PMAM3","PMAM4","PMET3","PMET5","PMET6","PNOR5","PNOR6","PNVL3","PNVL4","POMO3","POMO4","POPR4","PORP4","POSI3","PQUN3","PQUN4","PRBC3","PRBC4","PRGA4","PRIO3","PRML3","PRNR3","PRTX3","PRVI3","PSSA3","PTBL3","PTBL4","PTIP3","PTIP4","PTNT3","PTNT4","PTPA3","PTPA4","PTQS4","QGEP3","QUAL3","RADL3","RAIA3","RAIL3","RANI3","RANI4","RAPT3","RAPT4","RCSL4","RCTB31","RCTB33","RCTB41","RCTB42","RDCD3","RDNI3","RDTR3","REDE3","REDE4","REEM4","RENT3","REPA3","REPA4","RGEG3","RHDS3","RHDS4","RIPI3","RIPI4","RJCP3","RLOG3","RNAR3","RNEW11","RNEW3","RNEW4","RNPT3","RNPT4","ROMI3","ROMI4","RPAD3","RPAD5","RPAD6","RPMG3","RPMG4","RPSA4","RSID3","RSIP3","RSIP4","RSUL4","RUMO3","SALM3","SALM4","SANB11","SANB3","SANB4","SAPR11","SAPR3","SAPR4","SASG3","SBSP3","SCAR3","SCAR4","SCLO3","SCLO4","SDIA3","SDIA4","SEBB11","SEBB3","SEBB4","SEDU3","SEER3","SEMP3","SFSA3","SFSA4","SGAS3","SGAS4","SGEN3","SGEN4","SGPS3","SHOW3","SHUL4","SJOS3","SJOS4","SLCE3","SLCP3","SLED3","SLED4","SMLE3","SMLS3","SMTO3","SNSL3","SNSY5","SOND3","SOND5","SOND6","SPRI3","SPRI5","SPRI6","SQIA3","SSBR3","STBP11","STBP3","STLB3","STRP4","SUBA3","SULA11","SULA3","SULA4","SULT3","SULT4","SUZA4","SUZB3","SUZB5","SUZB6","SWET3","SZPQ4","TAEE11","TAEE3","TAEE4","TAMM3","TAMM4","TANC4","TARP11","TASA3","TASA4","TBLE3","TBLE5","TBLE6","TCNO3","TCNO4","TCOC3","TCOC4","TCSA3","TCSL4","TDBH3","TDBH4","TECN3","TEFC11","TEKA3","TEKA4","TELB3","TELB4","TEMP3","TEND3","TENE5","TENE7","TERI3","TESA3","TGMA3","TIBR3","TIBR5","TIBR6","TIET11","TIET3","TIET4","TIMP3","TKNO4","TLCP3","TLCP4","TMAR3","TMAR5","TMAR6","TMCP3","TMCP4","TMGC11","TMGC12","TMGC13","TMGC3","TMGC7","TNCP3","TNCP4","TNEP3","TNEP4","TNLP3","TNLP4","TOTS3","TOYB3","TOYB4","TPIS3","TPRC3","TPRC6","TRFO3","TRFO4","TRIS3","TROR3","TROR4","TRPL3","TRPL4","TRPN3","TSEP3","TSEP4","TSPP3","TSPP4","TUPY3","TUPY4","TVIT3","TXRX3","TXRX4","UBBR11","UBBR3","UBBR4","UCAS3","UCOP4","UGPA3","UGPA4","UNIP3","UNIP5","UNIP6","UOLL4","USIM3","USIM5","USIM6","VAGR3","VAGV3","VAGV4","VALE3","VALE5","VCPA4","VGOR3","VGOR4","VIGR3","VINE3","VINE5","VIVA3","VIVO3","VIVO4","VIVR3","VIVT3","VIVT4","VLID3","VNET3","VPSC3","VPSC4","VPTA3","VPTA4","VTLM3","VULC3","VULC4","VVAR11","VVAR3","VVAR4","VVAX3","VVAX4","WEGE3","WEGE4","WHRL3","WHRL4","WISA3","WISA4","WIZS3","WLMM3","WLMM4","WMBY3","WSON33","YDUQ3"]
for i in array:
    soup = make_soup('http://fundamentus.com.br/detalhes.php?papel='+i)
    for events in soup.findAll('table', {'class':'w728'}):
        for record in events.findAll('tr'):
            for data in record.findAll('td', 'data'):
                texto = data.text
                playerdata = playerdata + texto.strip() + ";"
    playerdata = playerdata + "\n"
header = "Papel;Cotacao;Tipo;Data ult cot;Empresa;Min 52 sem;Setor;Max 52 sem;Subsetor;Vol $ med (2m);Valor de mercado;Ult balanco processado;Valor da firma;Nro. Acoes;OSC dia;P/L;LPA;OSC Mes;P/VP;VPA;OSC 30 dias;P/EBIT;Marg. Bruta;OSC 12 meses;PSR;Mar. EBIT;OSC 2020;P/Ativos;Mar. Liquida;OSC 2019;P/CAP. Giro;EBIT / Ativo;OSC 2018;P/Ativ Circ Liq;ROIC;OSC 2017;Div. Yeld;ROE;OSC 2016; EV / EBITDA;Liquidez Corr;OSC 2015;EV / EBIT;Div Br/ Patrim;Vazio;Cresc.Rec (5a);Giro Ativos;Ativo;Div. Bruta;Disponibilidades;Div. Liquida;Ativo Circulante;Patrim. Liq;Receita Liquida (12m);Receita Liquida (3m);EBIT (12m);EBIT (3m);Lucro Liquido (12m);Lucro Liquido (3m)" + "\n"
file = open(os.path.expanduser("detalhepapeis.csv"), "wb")
file.write(bytes(header, encoding="ascii", errors='ignore'))
file.write(bytes(playerdata, encoding="ascii", errors='ignore'))