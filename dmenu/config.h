/* See LICENSE file for copyright and license details. */
/* Default settings; can be overriden by command line. */

static int topbar = 1;
static const char *fonts[] = {
	"JetBrainsMono Nerd Font:size=11"
};
static const char *prompt      = NULL;
static const char *colors[SchemeLast][2] = {
	[SchemeNorm] = { "#7d9fd4", "#05040e" },
	[SchemeSel]  = { "#05040e", "#ff2d8f" },
	[SchemeOut]  = { "#05040e", "#29c5e6" },
};
static unsigned int lines      = 10;
static const char worddelimiters[] = " ";
