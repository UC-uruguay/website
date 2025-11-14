<?php

if ( isset( $_POST['config_get'] ) && $_POST['config_get'] === 'true' ) {
	$responsive_mailform->config_get();
	exit;
}


if ( isset( $_POST['confirm_action'] ) && $_POST['confirm_action'] === 'on' ) {
	$responsive_mailform->post_check( 'confirm' );
	$responsive_mailform->confirm_set();
	exit;
}
